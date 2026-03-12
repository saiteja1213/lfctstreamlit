import streamlit as st
from datetime import datetime
from gsheets import append_row

st.title("Submit Your Prediction")

username = st.text_input("Name")
match = st.text_input("Match")
prediction = st.text_input("Prediction")
bold = st.checkbox("Bold Prediction")

if st.button("Submit"):
    row = [
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        username,
        match,
        prediction,
        bold,
        "pending",   # approval_status
        "pending",   # result_status
        0            # score
    ]
    append_row(row)
    st.success("Prediction saved!")
