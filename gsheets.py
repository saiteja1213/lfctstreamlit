import gspread
import pandas as pd
import json
import io
import streamlit as st
from google.oauth2.service_account import Credentials

# -----------------------------
# CONFIGURATION
# -----------------------------
SHEET_NAME = "LFxCT Scoreboard"  # your Google Sheet name
# -----------------------------

# Read the service account JSON from Streamlit secrets
service_account_info = json.loads(st.secrets["GOOGLESHEETAPI"])

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate using the secret JSON
creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

# Authorize client
client = gspread.authorize(creds)

# Get the first worksheet
def get_sheet():
    sheet = client.open(SHEET_NAME).sheet1
    return sheet

# Read all data as DataFrame
def read_data():
    sheet = get_sheet()
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

# Append a new row
def append_row(row):
    sheet = get_sheet()
    sheet.append_row(row)

# Update a specific cell
def update_cell(row, col, value):
    sheet = get_sheet()
    sheet.update_cell(row, col, value)
