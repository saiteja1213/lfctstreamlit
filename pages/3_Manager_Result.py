import streamlit as st
import pandas as pd

CSV_FILE = "predictions.csv"

st.title("Manager Results")

try:
    df = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    st.warning("No predictions yet.")
    st.stop()

approved = df[(df["approved"]==True) & (df["actual"].isna())]

for idx, row in approved.iterrows():
    st.write(f"{row['username']} | {row['match']} | {row['prediction']} | Bold: {row['bold']}")
    col1, col2 = st.columns(2)
    if col1.button("Correct", key=f"c{idx}"):
        df.at[idx, "actual"] = True
        df.at[idx, "score"] = 2 if row["bold"] else 1
        df.to_csv(CSV_FILE, index=False)
        st.experimental_rerun()
    if col2.button("Wrong", key=f"w{idx}"):
        df.at[idx, "actual"] = False
        df.at[idx, "score"] = 0
        df.to_csv(CSV_FILE, index=False)
        st.experimental_rerun()
