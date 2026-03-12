import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="Prediction League", layout="wide")

st.title("🏏 IPL Prediction League")

PRED_FILE = "predictions.csv"

# Create predictions file only if it does not exist
if not os.path.exists(PRED_FILE):

    df = pd.DataFrame(columns=[
        "timestamp",
        "username",
        "match",
        "prediction",
        "bold",
        "approval_status",
        "result_status",
        "score"
    ])

    df.to_csv(PRED_FILE, index=False)

st.write("Use the sidebar to navigate.")
