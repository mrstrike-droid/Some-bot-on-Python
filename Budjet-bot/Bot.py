import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Aleksey\\Desktop\\Python\\Automated borind staff\\Budjet-bot\\client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Бюджет")
list_of_hashes = sheet.get_worksheet(1)
for character in range_char("c", "y"):
    column_index = character
    print(column_index)
    list_of_hashes.update(f'{column_index}1', '01.08.2022')
input()

