from msilib import text
import telebot
from telebot import types
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from config import botoken
bot = telebot.TeleBot(botoken)
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Aleksey\\Desktop\\Python\\Automated borind staff\\Budjet-bot\\client_secret.json', scope)
client = gspread.authorize(creds)
day_today = str(date.today())
end = '\n'
sheet = client.open("Бюджет")
list_of_hashes = sheet.get_worksheet(1)
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Начать вносить покупки")
    keyboard.add(btn1)
@bot.message_handler(content_types=['text'])
def text_variant(message):
    if message.text == "Начать вносить покупки":
        choose_variant(message)
def choose_variant(message):
    for i in range(3,24):
        cell_info = list_of_hashes.cell(1, f'{i}').value
        if cell_info == None:
            update_info_in_next_day(message)
            break
        elif cell_info == day_today:
            update_info_again(message)
            break
def update_info_in_next_day(message):
    global i
    for i in range(3,24):
        cell_info = list_of_hashes.cell(1, f'{i}').value
        if cell_info == None:
            list_of_hashes.update_cell( 1, f'{i}', f'{day_today}')
            list_message(message)
            what_update()
            update_another()
            break
def update_info_again(message):
    global i
    for i in range(3,24):
        cell_info = list_of_hashes.cell(1, f'{i}').value
        if cell_info == day_today:
            bot.send_message(message.chat.id, 'hello')
            list_message(message)
            what_update()
            update_another()
            break
@bot.message_handler(commands=['List'])
def list_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #line_btn1 = ['Продукты', 'За квартиру']
    #btn1 = types.KeyboardButton("Продукты")
    #btn2 = types.KeyboardButton("За квартиру")
    btn3 = types.KeyboardButton("На кафе")
    #btn4 = types.KeyboardButton("Пицца на выходных")
    #btn5 = types.KeyboardButton("Прочие расходы")
    #btn6 = types.KeyboardButton("Личные деньги")
    #btn7 = types.KeyboardButton("Отложить")
    #btn8 = types.KeyboardButton("Сколько денег осталось")
    #keyboard.add(*line_btn1)
    keyboard.add(btn3)
    #keyboard.add(btn5, btn6)
    #keyboard.add(btn7, btn8)
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
def how_much_ramains():
    cell_amount = list_of_hashes.cell(15, f'{i}').value
    print(cell_amount)
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
bot.polling()
