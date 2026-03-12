import streamlit as st
import pandas as pd
from gsheets import read_data
from theme import apply_theme

apply_theme()
st.title("📊 My Stats & Past Predictions")

df = read_data()

if df.empty:
    st.info("No data yet. Submit your first prediction!")
    st.stop()

# Normalize column names: strip whitespace, lowercase
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Show actual columns in an expander for debugging
with st.expander("🔍 Debug: Sheet columns (click to verify)"):
    st.write(list(df.columns))

# Map common variations to expected names
COLUMN_MAP = {
    "match": "match_name",
    "matchname": "match_name",
    "user": "username",
    "user_name": "username",
    "name": "username",
    "predict": "prediction",
    "predicted": "prediction",
    "is_bold": "bold",
    "approval": "approval_status",
    "result": "result_status",
    "points": "score",
}
df.rename(columns=COLUMN_MAP, inplace=True)

# Check required columns exist
REQUIRED = ["username", "match_name", "prediction", "bold", "approval_status", "result_status", "score"]
missing = [c for c in REQUIRED if c not in df.columns]
if missing:
    st.error(f"Missing columns: {missing}  |  Actual columns: {list(df.columns)}")
    st.stop()

# Username picker
all_users = sorted(df["username"].unique().tolist())
selected_user = st.selectbox("Select your name", all_users)

user_df = df[df["username"] == selected_user].copy()

if user_df.empty:
    st.warning("No predictions found for this user.")
    st.stop()

# Normalize bold column — Google Sheets returns "TRUE"/"FALSE" strings
user_df["bold"] = user_df["bold"].apply(
    lambda x: True if str(x).strip().upper() == "TRUE" else False
)
# Normalize score column to numeric
user_df["score"] = pd.to_numeric(user_df["score"], errors="coerce").fillna(0)

# ── Stats bar ────────────────────────────────────────────────────────────────
total_preds     = len(user_df)
completed       = user_df[user_df["result_status"] == "completed"]
correct         = completed[completed["score"] > 0]
total_score     = int(user_df["score"].sum())
bold_preds      = int(user_df["bold"].sum())
accuracy        = round(len(correct) / len(completed) * 100, 1) if len(completed) > 0 else 0.0

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Points",   total_score)
c2.metric("Predictions",    total_preds)
c3.metric("Correct",        len(correct))
c4.metric("Accuracy",       f"{accuracy}%")
c5.metric("Bold Picks",     bold_preds)

st.markdown("<br>", unsafe_allow_html=True)

# ── Score over time chart (if plotly available) ───────────────────────────────
try:
    import plotly.express as px

    chart_df = completed.copy()
    chart_df["timestamp"] = pd.to_datetime(chart_df["timestamp"])
    chart_df = chart_df.sort_values("timestamp")
    chart_df["cumulative_score"] = chart_df["score"].cumsum()

    if not chart_df.empty:
        st.markdown("### 📈 Score Over Time")
        fig = px.area(
            chart_df, x="timestamp", y="cumulative_score",
            labels={"timestamp": "Date", "cumulative_score": "Cumulative Points"},
            color_discrete_sequence=["#b5e550"],
        )
        fig.update_layout(
            plot_bgcolor="#0d1f14", paper_bgcolor="#0d1f14",
            font_color="#e8f5ee", xaxis=dict(gridcolor="#1e3d28"),
            yaxis=dict(gridcolor="#1e3d28"), margin=dict(l=0, r=0, t=10, b=0),
        )
        st.plotly_chart(fig, use_container_width=True)
except ImportError:
    pass  # plotly not installed — skip chart

# ── Past predictions table ────────────────────────────────────────────────────
st.markdown("### 📋 All Predictions")

# Filter tabs
tab1, tab2, tab3, tab4 = st.tabs(["All", "✅ Correct", "❌ Incorrect", "⏳ Pending"])

def render_table(data):
    if data.empty:
        st.info("Nothing here yet.")
        return
    disp = data[["timestamp", "match", "prediction", "bold", "approval_status", "result_status", "score"]].copy()
    disp.columns = ["Time", "Match", "Prediction", "Bold", "Approval", "Result", "Score"]
    st.dataframe(disp, use_container_width=True, hide_index=True)

with tab1:
    render_table(user_df.sort_values("timestamp", ascending=False))
with tab2:
    render_table(correct.sort_values("timestamp", ascending=False))
with tab3:
    wrong = completed[completed["score"] == 0]
    render_table(wrong.sort_values("timestamp", ascending=False))
with tab4:
    pending = user_df[user_df["result_status"] == "pending"]
    render_table(pending.sort_values("timestamp", ascending=False))

# ── Bold prediction breakdown ─────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### ⚡ Bold vs Normal Breakdown")

bold_df   = completed[completed["bold"] == True]
normal_df = completed[completed["bold"] == False]

b1, b2 = st.columns(2)
with b1:
    bold_pts = int(bold_df["score"].sum())
    bold_correct = len(bold_df[bold_df["score"] > 0])
    st.markdown(f"""
    <div style="background:#132a1c; border:1px solid #1e3d28; border-radius:10px; padding:1.2rem;">
        <p style="color:#f5c842; font-weight:700; margin:0 0 0.5rem;">⚡ Bold Predictions</p>
        <p style="font-size:1.8rem; color:#e8f5ee; margin:0; font-weight:700;">{bold_pts} pts</p>
        <p style="color:#7aab8a; font-size:0.85rem; margin:0;">{bold_correct}/{len(bold_df)} correct</p>
    </div>
    """, unsafe_allow_html=True)
with b2:
    normal_pts = int(normal_df["score"].sum())
    normal_correct = len(normal_df[normal_df["score"] > 0])
    st.markdown(f"""
    <div style="background:#132a1c; border:1px solid #1e3d28; border-radius:10px; padding:1.2rem;">
        <p style="color:#b5e550; font-weight:700; margin:0 0 0.5rem;">🎯 Normal Predictions</p>
        <p style="font-size:1.8rem; color:#e8f5ee; margin:0; font-weight:700;">{normal_pts} pts</p>
        <p style="color:#7aab8a; font-size:0.85rem; margin:0;">{normal_correct}/{len(normal_df)} correct</p>
    </div>
    """, unsafe_allow_html=True)
