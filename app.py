import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="LFxCT season2", layout="wide")

st.title("LFxCT Season 2🏏")

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

st.write("Use the sidebar to navigate through the pages")
