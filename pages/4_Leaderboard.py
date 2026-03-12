import streamlit as st
from gsheets import read_data

st.title("Leaderboard")

df = read_data()
leaderboard = df.groupby("username")["score"].sum().reset_index()
leaderboard = leaderboard.sort_values("score", ascending=False)

st.dataframe(leaderboard, width='stretch')
