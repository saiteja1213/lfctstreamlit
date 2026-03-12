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

st.title("Manager Results")

df = pd.read_csv(PRED_FILE)

pending_results = df[
    (df["approval_status"] == "approved") &
    (df["result_status"] == "pending")
]

if pending_results.empty:
    st.success("No pending results")
    st.stop()

pending_results["correct"] = False

edited = st.data_editor(
    pending_results,
    column_config={"correct": st.column_config.CheckboxColumn()},
    use_container_width=True
)

if st.button("Submit Results"):

    for idx, row in edited.iterrows():

        if row["correct"]:

            df.loc[idx, "result_status"] = "completed"
            df.loc[idx, "score"] = 2 if row["bold"] else 1

        else:

            df.loc[idx, "result_status"] = "completed"
            df.loc[idx, "score"] = 0

    df.to_csv(PRED_FILE, index=False)

    st.success("Results Updated")
    st.rerun()
