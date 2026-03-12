import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

SHEET_NAME = "LFxCT Scoreboard"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "googlesheetapi.json",
    scope
)

client = gspread.authorize(creds)

def get_sheet():
    sheet = client.open(SHEET_NAME).sheet1
    return sheet

def read_data():
    sheet = get_sheet()
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

def append_row(row):
    sheet = get_sheet()
    sheet.append_row(row)

def update_cell(row, col, value):
    sheet = get_sheet()
    sheet.update_cell(row, col, value)
