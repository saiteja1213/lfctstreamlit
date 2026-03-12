import streamlit as st
import pandas as pd
from gsheets import read_data, update_cell
from theme import apply_theme

apply_theme()
st.title("✅ Manager Approval")

password_input = st.text_input("Enter Manager Password", type="password")
if password_input != st.secrets["MANAGER_PASSWORD"]:
    st.warning("Incorrect password! Access denied.")
    st.stop()

df = read_data()
pending = df[df["approval_status"] == "pending"].copy()

if pending.empty:
    st.success("🎉 No pending approvals — you're all caught up!")
    st.stop()

st.markdown(f"**{len(pending)} prediction(s) awaiting approval**")
pending["approve"] = False
edited = st.data_editor(pending, use_container_width=True)

if st.button("Approve Selected"):
    count = 0
    for idx, row in edited.iterrows():
        if row.get("approve"):
            update_cell(idx + 2, 6, "approved")
            count += 1
    st.success(f"✅ {count} prediction(s) approved!")
    st.rerun()
