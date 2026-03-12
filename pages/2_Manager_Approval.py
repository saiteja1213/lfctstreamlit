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
                st.success("Access Granted")
                st.rerun()
            else:
                st.error("Wrong password")

        st.stop()

check_password()

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
