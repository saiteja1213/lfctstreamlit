import streamlit as st
import pandas as pd
from datetime import datetime

CSV_FILE = "predictions.csv"
MATCHES_FILE = "matches.csv"

st.title("Submit Prediction")

# Load matches
try:
    matches_df = pd.read_csv(MATCHES_FILE)
except FileNotFoundError:
    st.warning("No matches file found.")
    st.stop()

# Filter matches for today
today_str = datetime.now().strftime("%m-%d-%Y")
today_matches = matches_df[matches_df["match_date"] == today_str]

if today_matches.empty:
    st.info("No matches today.")
    st.stop()

# Dropdown for today's matches
match = st.selectbox("Select Match", today_matches["match_name"].tolist())

username = st.text_input("Your Name")
prediction = st.text_input("Prediction (Win/Lose/Draw)")
bold = st.checkbox("Bold Prediction (double points)")

if st.button("Submit Prediction"):
    timestamp = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    new_row = {
        "timestamp": timestamp,
        "username": username,
        "match": match,
        "prediction": prediction,
        "bold": bold,
        "approved": False,
        "actual": None,
        "score": 0
    }

    try:
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([new_row])

    df.to_csv(CSV_FILE, index=False)
    st.success("Prediction submitted!")
