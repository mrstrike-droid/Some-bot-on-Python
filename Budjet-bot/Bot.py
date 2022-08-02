import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import numpy as np
from datetime import date
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Aleksey\\Desktop\\Python\\Automated borind staff\\Budjet-bot\\client_secret.json', scope)
client = gspread.authorize(creds)
day_today = str(date.today())
sheet = client.open("Бюджет")
list_of_hashes = sheet.get_worksheet(1)
def update_info_in_next_day():
    global i
    for i in range(3,24):
        cell_info = list_of_hashes.cell(1, f'{i}').value
        if cell_info == None:
            list_of_hashes.update_cell( 1, f'{i}', f'{day_today}')
            break
def insert_info_in_cell_and_get_residue():
    print('Что мы потратили сегодня на продукты:')
    product = int(input())
    list_of_hashes.update_cell( 2, f'{i}', f'{product}')
    cell_info = list_of_hashes.cell(2, 2).value
    print('На продукты осталось: ', cell_info)
update_info_in_next_day()
insert_info_in_cell_and_get_residue()
def update_info_again():
    global i
    for i in range(3,24):
        cell_info = list_of_hashes.cell(1, f'{i}').value
        if cell_info == day_today:
            list_of_hashes.update_cell( 2, f'{i}', 'Done')
            break
#update_info_again()
#insert_info_in_cell_and_get_residue()

