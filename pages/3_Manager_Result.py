import streamlit as st
import pandas as pd

PRED_FILE = "predictions.csv"
PASSWORD = "ipladmin"

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

st.title("Manager Results")

df = pd.read_csv(PRED_FILE)

pending = df[
    (df["approval_status"]=="approved") &
    (df["result_status"]=="pending")
].copy()

if pending.empty:
    st.success("No pending results")
    st.stop()

pending["correct"] = False

edited = st.data_editor(
    pending,
    use_container_width=True,
    column_config={
        "correct": st.column_config.CheckboxColumn("Correct")
    },
    disabled=[
        "timestamp","username","match",
        "prediction","bold",
        "approval_status","result_status","score"
    ]
)

if st.button("Submit Results"):

    for idx,row in edited.iterrows():

        if row["correct"]:
            df.loc[idx,"score"] = 2 if row["bold"] else 1
        else:
            df.loc[idx,"score"] = 0

        df.loc[idx,"result_status"] = "completed"

    df.to_csv(PRED_FILE,index=False)

    st.success("Results updated")

    st.rerun()
