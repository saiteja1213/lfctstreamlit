import streamlit as st
import pandas as pd
from datetime import datetime
from gsheets import append_row
from theme import apply_theme

apply_theme()
st.title("📝 Submit Prediction")

matches_df = pd.read_csv("matches.csv")
matches_df["match_date"] = pd.to_datetime(matches_df["match_date"], format="%m-%d-%Y")

today = datetime.today().date()
today_matches = matches_df[matches_df["match_date"].dt.date == today]

if today_matches.empty:
    st.warning("No matches scheduled for today. Check the Match Schedule page for upcoming fixtures!")
else:
    st.markdown(f"<p style='color:#7aab8a;'>Today — {today.strftime('%B %d, %Y')}</p>", unsafe_allow_html=True)

    with st.form("prediction_form"):
        selected_match = st.selectbox("Select Match", today_matches["match_name"])
        username = st.text_input("Your Name")
        prediction = st.text_input("Your Prediction (team you think will win)")
        bold = st.checkbox("⚡ Bold Prediction — double points if correct!")

        submitted = st.form_submit_button("Submit Prediction")

    if submitted:
        if not username.strip() or not prediction.strip():
            st.error("Please fill in your name and prediction.")
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            row = [timestamp, username.strip(), selected_match, prediction.strip(), bold, "pending", "pending", 0]
            append_row(row)
            st.success(f"✅ Prediction submitted for **{selected_match}**!")
            if bold:
                st.info("⚡ Bold prediction locked in — double points on the line!")
