import streamlit as st
import pandas as pd

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
