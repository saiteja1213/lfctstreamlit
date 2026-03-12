import streamlit as st
import pandas as pd

PRED_FILE = "predictions.csv"

st.title("Leaderboard")

df = pd.read_csv(PRED_FILE)

leaderboard = df.groupby("username")["score"].sum().reset_index()

leaderboard = leaderboard.sort_values("score", ascending=False)

st.dataframe(leaderboard, use_container_width=True)
