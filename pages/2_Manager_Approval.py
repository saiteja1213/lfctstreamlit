import streamlit as st
import pandas as pd

MANAGER_PASSWORD = "admin"

def check_password():
    if "manager_auth" not in st.session_state:
        st.session_state.manager_auth = False

    if not st.session_state.manager_auth:
        password = st.text_input("Manager Password", type="password")

        if st.button("Login"):
            if password == MANAGER_PASSWORD:
                st.session_state.manager_auth = True
                st.rerun()
            else:
                st.error("Wrong password")

        st.stop()

check_password()

st.title("Manager Approval")

df = pd.read_csv("predictions.csv")

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
        "timestamp",
        "username",
        "match",
        "prediction",
        "bold",
        "approval_status",
        "result_status",
        "score"
    ]
)

if st.button("Approve Selected"):

    selected = edited[edited["approve"] == True]

    for idx in selected.index:
        df.loc[idx, "approval_status"] = "approved"

    df.to_csv("predictions.csv", index=False)

    st.success("Predictions Approved")
    st.rerun()
