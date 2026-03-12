import streamlit as st
import pandas as pd

PRED_FILE = "predictions.csv"

st.title("Manager Approval")

df = pd.read_csv(PRED_FILE)

pending = df[df["approval_status"] == "pending"]

if pending.empty:
    st.success("No pending approvals")
    st.stop()

st.write("Pending Predictions")

pending["approve"] = False

edited = st.data_editor(
    pending,
    column_config={"approve": st.column_config.CheckboxColumn()},
    use_container_width=True
)

if st.button("Approve Selected"):

    approve_rows = edited[edited["approve"] == True]

    for idx in approve_rows.index:
        df.loc[idx, "approval_status"] = "approved"

    df.to_csv(PRED_FILE, index=False)

    st.success("Approved Successfully")
    st.rerun()
