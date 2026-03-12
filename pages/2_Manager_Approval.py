import streamlit as st
import pandas as pd
from gsheets import read_data, update_cell

st.title("Manager Approval")
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
pending = df[df["approval_status"] == "pending"].copy()

if pending.empty:
    st.success("No pending approvals")
    st.stop()

pending.loc[:,"approve"] = False

edited = st.data_editor(pending, width='stretch')

if st.button("Approve Selected"):
    for idx, row in edited.iterrows():
        if row.get("approve"):
            update_cell(idx + 2, 6, "approved")  # approval_status column = 6
    st.success("Approved!")
    st.rerun()
