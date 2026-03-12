import streamlit as st
import pandas as pd
from datetime import datetime
from gsheets import append_row  # or your local append_row function

st.title("Submit Prediction")

# Load matches from CSV
matches_df = pd.read_csv("matches.csv")

# Convert match_date to datetime
matches_df["match_date"] = pd.to_datetime(matches_df["match_date"], format="%m-%d-%Y")

# Filter only today's matches
today = datetime.today().date()
today_matches = matches_df[matches_df["match_date"].dt.date == today]

if today_matches.empty:
    st.warning("No matches scheduled for today!")
else:
    # Dropdown for match selection
    selected_match = st.selectbox("Select Match", today_matches["match"])

    username = st.text_input("Your Name")
    prediction = st.text_input("Your Prediction")
    bold = st.checkbox("Bold Prediction (double points)")

    if st.button("Submit"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [
            timestamp,
            username,
            selected_match,
            prediction,
            bold,
            "pending",  # approval
            "pending",  # result
            0           # score
        ]
        append_row(row)  # write to your predictions sheet/csv
        st.success(f"Prediction for {selected_match} submitted!")
