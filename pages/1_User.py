import streamlit as st
import pandas as pd
import os
from datetime import datetime

PRED_FILE = "predictions.csv"
MATCH_FILE = "matches.csv"

st.title("Submit Prediction")

# ensure predictions file exists
if not os.path.exists(PRED_FILE):
    df = pd.DataFrame(columns=[
        "timestamp","username","match","prediction",
        "bold","approval_status","result_status","score"
    ])
    df.to_csv(PRED_FILE,index=False)

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

    df = pd.read_csv(PRED_FILE)

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_csv(PRED_FILE, index=False)

    st.success("Prediction submitted!")
