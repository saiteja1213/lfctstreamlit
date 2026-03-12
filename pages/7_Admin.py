import streamlit as st
import pandas as pd
from gsheets import read_data, update_cell
from theme import apply_theme

apply_theme()
st.title("⚙️ Admin Panel")

password_input = st.text_input("Enter Admin Password", type="password")
if password_input != st.secrets["ADMIN_PASSWORD"]:
    st.warning("Incorrect password! Access denied.")
    st.stop()

st.success("Access granted.")

df = read_data()
st.markdown(f"**{len(df)} total records in sheet**")
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

if st.button("💾 Save Changes"):
    for idx, row in edited_df.iterrows():
        for col_idx, col_name in enumerate(df.columns):
            update_cell(idx + 2, col_idx + 1, row[col_name])
    st.success("Sheet updated!")
    st.rerun()
