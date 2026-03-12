import streamlit as st
import pandas as pd
from gsheets import read_data, update_cell
from theme import apply_theme

apply_theme()
st.title("🎯 Manager Results")

password_input = st.text_input("Enter Manager Password", type="password")
if password_input != st.secrets["MANAGER_PASSWORD"]:
    st.warning("Incorrect password! Access denied.")
    st.stop()

df = read_data()
pending = df[(df["approval_status"] == "approved") & (df["result_status"] == "pending")].copy()

if pending.empty:
    st.success("🎉 No pending results — all done!")
    st.stop()

st.markdown(f"**{len(pending)} prediction(s) awaiting results**")
pending["correct"] = False
edited = st.data_editor(pending, use_container_width=True)

if st.button("Submit Results"):
    for idx, row in edited.iterrows():
        sheet_row = idx + 2
        score = (2 if row["bold"] else 1) if row.get("correct") else 0
        update_cell(sheet_row, 7, "completed")
        update_cell(sheet_row, 8, score)
    st.success("Results updated!")
    st.rerun()
