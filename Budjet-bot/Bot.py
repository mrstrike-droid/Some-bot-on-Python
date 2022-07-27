import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Aleksey\\Desktop\\Python\\Automated borind staff\\Budjet-bot\\client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Бюджет")
list_of_hashes = sheet.get_worksheet(1)
list_of_hashes = list_of_hashes.get_all_records()
print(list_of_hashes)
input()

