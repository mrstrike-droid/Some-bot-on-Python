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
            text_message()
            what_update()
            update_another()
            break
def product_info():
    print('Что мы потратили сегодня на продукты:')
    amount = int(input())
    list_of_hashes.update_cell( 2, f'{i}', f'{amount}')
    cell_info = list_of_hashes.cell(2, 2).value
    print('На продукты осталось: ', cell_info)
def product_info_add_next():
    cell_amount = int(list_of_hashes.cell(2, f'{i}').value)
    print('Сколько еще потратили на продукты:')
    amount_new = int(input())
    amount_all = amount_new + cell_amount
    list_of_hashes.update_cell(2, f'{i}', f'{amount_all}')
    cell_info = list_of_hashes.cell(2, 2).value
    print('На продукты осталось: ', cell_info)
def flat_info():
    print('Что мы потратили сегодня на квартиру:')
    amount = int(input())
    list_of_hashes.update_cell(3, f'{i}', f'{amount}')
    cell_info = list_of_hashes.cell(3, 2).value
    print('На квартиру осталось: ', cell_info)
def flat_info_add_next():
    cell_amount = int(list_of_hashes.cell(3, f'{i}').value)
    print('Сколько еще потратили на квартиру:')
    amount_new = int(input())
    amount_all = amount_new + cell_amount
    list_of_hashes.update_cell( 3, f'{i}', f'{amount_all}')
    cell_info = list_of_hashes.cell(3, 2).value
    print('На квартиру осталось: ', cell_info)
def cafe_info():
    print('Что мы потратили сегодня на кафе:')
    amount = int(input())
    list_of_hashes.update_cell( 4, f'{i}', f'{amount}')
    cell_info = list_of_hashes.cell(4, 2).value
    print('На кафе осталось: ', cell_info)
def cafe_info_add_next():
    cell_amount = int(list_of_hashes.cell(4, f'{i}').value)
    print('Сколько еще потратили на кафе:')
    amount_new = int(input())
    amount_all = amount_new + cell_amount
    list_of_hashes.update_cell(4, f'{i}', f'{amount_all}')
    cell_info = list_of_hashes.cell(4, 2).value
    print('На кафе осталось: ', cell_info)
def pizza_info():
    print('Что мы потратили сегодня на пиццу:')
    amount = int(input())
    list_of_hashes.update_cell( 5, f'{i}', f'{amount}')
    cell_info = list_of_hashes.cell(5, 2).value
    print('На пиццу осталось: ', cell_info)
def pizza_info_add_next():
    cell_amount = int(list_of_hashes.cell(5, f'{i}').value)
    print('Сколько еще потратили на пиццу:')
    amount_new = int(input())
    amount_all = amount_new + cell_amount
    list_of_hashes.update_cell(5, f'{i}', f'{amount_all}')
    cell_info = list_of_hashes.cell(5, 2).value
    print('На пиццу осталось: ', cell_info)
def another_info():
    print('Что мы потратили сегодня на прочие расходы:')
    amount = int(input())
    list_of_hashes.update_cell( 6, f'{i}', f'{amount}')
    cell_info = list_of_hashes.cell(6, 2).value
    print('На прочие расходы осталось: ', cell_info)
def another_info_add_next():
    cell_amount = int(list_of_hashes.cell(6, f'{i}').value)
    print('Сколько еще потратили на прочие расходы:')
    amount_new = int(input())
    amount_all = amount_new + cell_amount
    list_of_hashes.update_cell(6, f'{i}', f'{amount_all}')
    cell_info = list_of_hashes.cell(6, 2).value
    print('На прочие расходы осталось: ', cell_info)
def self_pay_info():
    print('Что мы потратили сегодня на личные нужды:')
    amount = int(input())
    list_of_hashes.update_cell( 7, f'{i}', f'{amount}')
    cell_info = list_of_hashes.cell(7, 2).value
    print('На личные нужды осталось: ', cell_info)
def self_pay_info_add_next():
    cell_amount = int(list_of_hashes.cell(7, f'{i}').value)
    print('Сколько еще потратили на личные нужды:')
    amount_new = int(input())
    amount_all = amount_new + cell_amount
    list_of_hashes.update_cell(7, f'{i}', f'{amount_all}')
    cell_info = list_of_hashes.cell(7, 2).value
    print('На личные нужды осталось: ', cell_info)
def saving_info():
    print('Что мы отложили сегодня:')
    amount = int(input())
    list_of_hashes.update_cell( 8, f'{i}', f'{amount}')
    cell_info = list_of_hashes.cell(8, f'{i}').value
    print('На данный момет мы отложили: ', cell_info)
def saving_info_add_next():
    cell_amount = int(list_of_hashes.cell(8, f'{i}').value)
    print('Сколько еще потложили сегодня:')
    amount_new = int(input())
    amount_all = amount_new + cell_amount
    list_of_hashes.update_cell(8, f'{i}', f'{amount_all}')
    cell_info = list_of_hashes.cell(8, f'{i}').value
    print('На данный момет мы отложили: ', cell_info)
def text_message():
    global end
    end = '\n'
    print('На что сегодня потратили:'+end+'1 - продукты'+end+'2 - на квартиру'+end+'3 - на кафе'+end+'4 - на пиццу'+end+'5 - на прочие расходы'+end+'6 - на личные нужды'+end+'7 - отложили'+end+'8 - Узнать сколько осталось денег всего')
def what_update():
    variant = int(input())
    if variant == 1:
        cell_amount = list_of_hashes.cell(2, f'{i}').value
        if cell_amount == None:
            product_info()
        elif cell_amount != 0:
            product_info_add_next()
    elif variant == 2:
        cell_amount = list_of_hashes.cell(3, f'{i}').value
        if cell_amount == None:
            flat_info()
        elif cell_amount != 0:
            flat_info_add_next()
    elif variant == 3:
        cell_amount = list_of_hashes.cell(4, f'{i}').value
        if cell_amount == None:
            cafe_info()
        elif cell_amount != 0:
            cafe_info_add_next()
    elif variant == 4:
        cell_amount = list_of_hashes.cell(5, f'{i}').value
        if cell_amount == None:
            pizza_info()
        elif cell_amount != 0:
            pizza_info_add_next()
    elif variant == 5:
        cell_amount = list_of_hashes.cell(6, f'{i}').value
        if cell_amount == None:
            another_info()
        elif cell_amount != 0:
            another_info_add_next()
    elif variant == 6:
        cell_amount = list_of_hashes.cell(7, f'{i}').value
        if cell_amount == None:
            self_pay_info()
        elif cell_amount != 0:
            self_pay_info_add_next()
    elif variant == 7:
        cell_amount = list_of_hashes.cell(8, f'{i}').value
        if cell_amount == None:
            saving_info()
        elif cell_amount != 0:
            saving_info_add_next()
    elif variant == 8:
        how_much_ramains()
def update_another():
    while True:
        print('Что то еще: '+end+'1 - Да'+end+'2 - Нет'+end+'3 - Узнать сколько осталось денег всего')
        answer = int(input())
        if answer == 1:
            print('1 - продукты'+end+'2 - на квартиру'+end+'3 - на кафе'+end+'4 - на пиццу'+end+'5 - на прочие расходы'+end+'6 - на личные нужды'+end+'7 - отложили')
            what_update()
        elif answer == 2:
            break
        elif answer == 3:
            how_much_ramains()
def how_much_ramains():
    cell_amount = list_of_hashes.cell(15, f'{i}').value
    print(cell_amount)
def update_info_again():
    global i
    for i in range(3,24):
        cell_info = list_of_hashes.cell(1, f'{i}').value
        if cell_info == day_today:
            text_message()
            what_update()
            update_another()
            break
#update_info_in_next_day()
update_info_again()




