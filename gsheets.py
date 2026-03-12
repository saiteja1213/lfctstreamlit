import json
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
import streamlit as st

SHEET_NAME = "LFxCT Scoreboard"

# Load secret
service_account_info = json.loads(st.secrets["GOOGLESHEETAPI"])

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
client = gspread.authorize(creds)

def get_sheet():
    return client.open(SHEET_NAME).sheet1

def read_data():
    sheet = get_sheet()
    return pd.DataFrame(sheet.get_all_records())

def append_row(row):
    sheet = get_sheet()
    sheet.append_row(row)

def update_cell(row, col, value):
    sheet = get_sheet()
    sheet.update_cell(row, col, value)
