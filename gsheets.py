import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# -----------------------------
# CONFIGURATION
# -----------------------------
SHEET_NAME = "LFxCT Scoreboard"  # your sheet name
SERVICE_ACCOUNT_FILE = "lfxct-489919-b651761e0290.json"  # downloaded JSON key
# -----------------------------

# Set scopes
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate with service account
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

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
