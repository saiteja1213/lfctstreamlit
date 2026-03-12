import streamlit as st
import pandas as pd
from gsheets import read_data, update_cell

st.title("Manager Results")
password_input = st.text_input("Enter Manager Password", type="password")

if password_input != st.secrets["MANAGER_PASSWORD"]:
    st.warning("Incorrect password! Access denied.")
    st.stop()  # Stop page if password is wrong
    
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    pw = st.text_input("Manager Password", type="password")
    if st.button("Login"):
        if pw == PASSWORD:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Wrong password")
    st.stop()

df = read_data()
pending = df[(df["approval_status"]=="approved") & (df["result_status"]=="pending")].copy()

if pending.empty:
    st.success("No pending results")
    st.stop()

pending.loc[:,"correct"] = False
edited = st.data_editor(pending,width='stretch')

if st.button("Submit Results"):
    for idx, row in edited.iterrows():
        sheet_row = idx + 2
        if row.get("correct"):
            score = 2 if row["bold"] else 1
        else:
            score = 0
        update_cell(sheet_row, 7, "completed")  # result_status
        update_cell(sheet_row, 8, score)       # score
    st.success("Results updated!")
    st.rerun()
