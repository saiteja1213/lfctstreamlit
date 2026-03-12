import streamlit as st
import pandas as pd

CSV_FILE = "predictions.csv"

st.title("Manager Approval")

try:
    df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    st.warning("No predictions yet.")
    st.stop()

pending = df[df["approved"]==False]

for idx, row in pending.iterrows():
    st.write(f"{row['username']} | {row['match']} | {row['prediction']} | Bold: {row['bold']}")
    if st.button(f"Approve {row['username']} - {row['match']}", key=idx):
        df.at[idx, "approved"] = True
        df.to_csv(CSV_FILE, index=False)
        st.experimental_rerun()
