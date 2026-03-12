import streamlit as st
import pandas as pd
from datetime import datetime

CSV_FILE = "predictions.csv"

st.title("Submit Prediction")

username = st.text_input("Your Name")
match = st.text_input("Match (e.g., Liverpool vs Arsenal)")
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
