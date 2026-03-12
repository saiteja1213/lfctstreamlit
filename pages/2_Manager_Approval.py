import streamlit as st
import pandas as pd
import os

PRED_FILE = "predictions.csv"
PASSWORD = "ipladmin"

# password protection
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

st.title("Manager Approval")

df = pd.read_csv(PRED_FILE)

pending = df[df["approval_status"] == "pending"].copy()

if pending.empty:
    st.success("No pending approvals")
    st.stop()

pending["approve"] = False

edited = st.data_editor(
    pending,
    use_container_width=True,
    column_config={
        "approve": st.column_config.CheckboxColumn("Approve")
    },
    disabled=[
        "timestamp","username","match",
        "prediction","bold",
        "approval_status","result_status","score"
    ]
)

if st.button("Approve Selected"):

    selected = edited[edited["approve"] == True]

    for idx in selected.index:
        df.loc[idx,"approval_status"] = "approved"

    df.to_csv(PRED_FILE,index=False)

    st.success("Predictions Approved")

    st.rerun()
