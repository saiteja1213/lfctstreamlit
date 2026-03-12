import streamlit as st
import pandas as pd
from gsheets import read_data, update_cell, append_row

st.title("Admin Panel")
ADMIN_PASSWORD = "admin123"

if "admin_auth" not in st.session_state:
    st.session_state.admin_auth = False

if not st.session_state.admin_auth:
    pw = st.text_input("Admin Password", type="password")
    if st.button("Login"):
        if pw == ADMIN_PASSWORD:
            st.session_state.admin_auth = True
            st.rerun()
        else:
            st.error("Wrong password")
    st.stop()

df = read_data()
edited_df = st.data_editor(df, num_rows="dynamic", width='stretch')

if st.button("Save Changes"):
    for idx, row in edited_df.iterrows():
        for col_idx, col_name in enumerate(df.columns):
            update_cell(idx + 2, col_idx + 1, row[col_name])
    st.success("Sheet Updated!")
    st.rerun()
