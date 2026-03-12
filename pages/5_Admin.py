import streamlit as st
import pandas as pd
import os

PRED_FILE = "predictions.csv"
ADMIN_PASSWORD = "admin123"

st.title("Admin Panel")

# password protection
if "admin_auth" not in st.session_state:
    st.session_state.admin_auth = False

if not st.session_state.admin_auth:

    password = st.text_input("Enter Admin Password", type="password")

    if st.button("Login"):
        if password == ADMIN_PASSWORD:
            st.session_state.admin_auth = True
            st.rerun()
        else:
            st.error("Wrong password")

    st.stop()

st.success("Admin Logged In")

# ensure file exists
if not os.path.exists(PRED_FILE):

    df = pd.DataFrame(columns=[
        "timestamp",
        "username",
        "match",
        "prediction",
        "bold",
        "approval_status",
        "result_status",
        "score"
    ])

    df.to_csv(PRED_FILE, index=False)

# load sheet
df = pd.read_csv(PRED_FILE)

st.subheader("Edit Predictions Table")

edited_df = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True
)

if st.button("Save Changes"):

    edited_df.to_csv(PRED_FILE, index=False)

    st.success("Sheet Updated Successfully")

    st.rerun()

st.download_button(
    "Download CSV",
    edited_df.to_csv(index=False),
    "predictions.csv",
    "text/csv"
)
