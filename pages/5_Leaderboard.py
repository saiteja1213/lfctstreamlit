import streamlit as st
import pandas as pd
from gsheets import read_data
from theme import apply_theme

apply_theme()
st.title("🏆 Leaderboard")

df = read_data()

if df.empty:
    st.info("No predictions yet. Be the first to submit!")
    st.stop()

leaderboard = df.groupby("username").agg(
    total_score=("score", "sum"),
    predictions=("username", "count"),
    correct=("result_status", lambda x: (x == "completed").sum()),
).reset_index()

# Correct count: only rows that scored > 0 and are completed
completed = df[df["result_status"] == "completed"]
correct_counts = completed[completed["score"] > 0].groupby("username").size().reset_index(name="correct")
leaderboard = leaderboard.drop(columns=["correct"])
leaderboard = leaderboard.merge(correct_counts, on="username", how="left").fillna(0)
leaderboard["correct"] = leaderboard["correct"].astype(int)
leaderboard["accuracy"] = (leaderboard["correct"] / leaderboard["predictions"].replace(0, 1) * 100).round(1)
leaderboard = leaderboard.sort_values("total_score", ascending=False).reset_index(drop=True)

# Medals
medals = ["🥇", "🥈", "🥉"]

st.markdown("<br>", unsafe_allow_html=True)

# Top 3 podium
top3 = leaderboard.head(3)
cols = st.columns(3)
for i, (col, (_, row)) in enumerate(zip(cols, top3.iterrows())):
    with col:
        st.markdown(f"""
        <div style="background:#132a1c; border:1px solid #1e3d28; border-radius:12px;
                    padding:1.5rem; text-align:center;">
            <div style="font-size:2rem;">{medals[i] if i < len(medals) else ''}</div>
            <div style="font-family:'Bebas Neue',sans-serif; font-size:1.4rem;
                        color:#b5e550; letter-spacing:2px; margin:0.3rem 0;">
                {row['username']}
            </div>
            <div style="font-size:2rem; font-weight:700; color:#e8f5ee;">
                {int(row['total_score'])}
            </div>
            <div style="color:#7aab8a; font-size:0.8rem;">pts</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Full table
st.markdown("### Full Rankings")
display = leaderboard.copy()
display.index = display.index + 1
display.columns = ["Player", "Points", "Predictions", "Correct", "Accuracy %"]
st.dataframe(display, use_container_width=True)
