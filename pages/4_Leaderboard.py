import streamlit as st
import pandas as pd

CSV_FILE = "predictions.csv"

st.title("Leaderboard")

try:
    df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    st.warning("No predictions yet.")
    st.stop()

leaderboard = df.groupby("username")["score"].sum().reset_index()
leaderboard = leaderboard.sort_values(by="score", ascending=False)
st.table(leaderboard)
