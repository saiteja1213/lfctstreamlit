import streamlit as st
import pandas as pd
from datetime import datetime

PRED_FILE = "predictions.csv"
MATCH_FILE = "matches.csv"

st.title("Submit Prediction")

matches = pd.read_csv(MATCH_FILE)

today = datetime.now().strftime("%m-%d-%Y")
today_matches = matches[matches["match_date"] == today]

if today_matches.empty:
    st.warning("No matches today")
    st.stop()

match = st.selectbox("Select Match", today_matches["match_name"])

username = st.text_input("Your Name")
prediction = st.text_input("Prediction")
bold = st.checkbox("Bold Prediction (2 points)")

if st.button("Submit Prediction"):

    new_row = {
        "timestamp": datetime.now().strftime("%m-%d-%Y %H:%M"),
        "username": username,
        "match": match,
        "prediction": prediction,
        "bold": bold,
        "approval_status": "pending",
        "result_status": "pending",
        "score": 0
    }

    try:
        df = pd.read_csv(PRED_FILE)
    except:
        df = pd.DataFrame(columns=new_row.keys())

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_csv(PRED_FILE, index=False)

    st.success("Prediction submitted!")
