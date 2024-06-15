import gspread,requests,time
import math
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "your google sheet id" #after /d/...sheet_id...../ 
workbook = client.open_by_key(sheet_id) 
targetSheet = workbook.worksheet("sheet name") #change

records = targetSheet.get_all_records()
