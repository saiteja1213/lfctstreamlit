import streamlit as st
import pandas as pd
from datetime import datetime
from theme import apply_theme

apply_theme()
st.title("📅 Match Schedule")

matches_df = pd.read_csv("matches.csv")
matches_df["match_date"] = pd.to_datetime(matches_df["match_date"], format="%m-%d-%Y")
matches_df = matches_df.sort_values("match_date")

today = datetime.today().date()

# Split into sections
past     = matches_df[matches_df["match_date"].dt.date <  today]
today_m  = matches_df[matches_df["match_date"].dt.date == today]
upcoming = matches_df[matches_df["match_date"].dt.date >  today]

def render_match_card(row, tag=""):
    date_str = row["match_date"].strftime("%a, %d %b %Y")
    teams = row["match_name"].split(" vs ")
    team1 = teams[0].strip() if len(teams) == 2 else row["match_name"]
    team2 = teams[1].strip() if len(teams) == 2 else ""
    st.markdown(f"""
    <div style="background:#132a1c; border:1px solid #1e3d28; border-radius:10px;
                padding:1rem 1.4rem; margin-bottom:0.6rem; display:flex;
                justify-content:space-between; align-items:center;">
        <div>
            <span style="font-size:1.05rem; font-weight:600; color:#e8f5ee;">
                {team1}
            </span>
            <span style="color:#7aab8a; margin:0 0.6rem;">vs</span>
            <span style="font-size:1.05rem; font-weight:600; color:#e8f5ee;">
                {team2}
            </span>
        </div>
        <div style="text-align:right;">
            <span style="color:#7aab8a; font-size:0.85rem;">{date_str}</span>
            {"&nbsp;&nbsp;<span style='background:#1a4a2e;color:#b5e550;padding:2px 10px;border-radius:20px;font-size:0.75rem;font-weight:600;letter-spacing:1px;'>TODAY</span>" if tag == "today" else ""}
        </div>
    </div>
    """, unsafe_allow_html=True)

# Today
if not today_m.empty:
    st.markdown("### 🟢 Today's Matches")
    for _, row in today_m.iterrows():
        render_match_card(row, tag="today")
    st.markdown("<br>", unsafe_allow_html=True)

# Upcoming
if not upcoming.empty:
    st.markdown("### 🗓️ Upcoming Matches")
    # Group by date
    for date, group in upcoming.groupby(upcoming["match_date"].dt.date):
        st.markdown(f"<p style='color:#7aab8a; font-size:0.85rem; margin:0.8rem 0 0.3rem; letter-spacing:1px;'>{date.strftime('%A, %d %B %Y').upper()}</p>", unsafe_allow_html=True)
        for _, row in group.iterrows():
            render_match_card(row)
    st.markdown("<br>", unsafe_allow_html=True)

# Past
if not past.empty:
    with st.expander("📜 Past Matches"):
        for _, row in past.sort_values("match_date", ascending=False).iterrows():
            render_match_card(row)
