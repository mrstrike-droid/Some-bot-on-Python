from email import message
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
    bot.send_message(message.chat.id, text='Выбери что сегодня смотрим.'.format(message.from_user), reply_markup=keyboard)
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
            break
def update_info_again(message):
    global i
    for i in range(3,24):
        cell_info = list_of_hashes.cell(1, f'{i}').value
        if cell_info == day_today:
            list_message(message)
            break
@bot.message_handler(commands=['List'])
def list_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    line_btn1 = ['Продукты', 'За квартиру']
    line_btn2 = ['На кафе', 'Пицца']
    line_btn3 = ['Прочие расходы', 'Личные расходы']
    line_btn4 = ['Отложить', 'Сколько осталось']
    keyboard.add(*line_btn1)
    keyboard.add(*line_btn2)
    keyboard.add(*line_btn3)
    keyboard.add(*line_btn4)
    bot.send_message(message.chat.id, text='Выбери что сегодня смотрим.'.format(message.from_user), reply_markup=keyboard)
    bot.register_next_step_handler(message, what_update)
@bot.message_handler(content_types=['text'])
def what_update(message):
    if message.text == 'Продукты':
        cell_amount = list_of_hashes.cell(2, f'{i}').value
        if cell_amount == None:
            product_info(message)
        elif cell_amount != 0:
            product_info_add_next(message)
    elif message.text == 'За квартиру':
        cell_amount = list_of_hashes.cell(3, f'{i}').value
        if cell_amount == None:
            flat_info()
        elif cell_amount != 0:
            flat_info_add_next()
    elif message.text == 'На кафе':
        cell_amount = list_of_hashes.cell(4, f'{i}').value
        if cell_amount == None:
            cafe_info()
        elif cell_amount != 0:
            cafe_info_add_next()
    elif message.text == 'Пицца':
        cell_amount = list_of_hashes.cell(5, f'{i}').value
        if cell_amount == None:
            pizza_info()
        elif cell_amount != 0:
            pizza_info_add_next()
    elif message.text == 'Прочие расходы':
        cell_amount = list_of_hashes.cell(6, f'{i}').value
        if cell_amount == None:
            another_info()
        elif cell_amount != 0:
            another_info_add_next()
    elif message.text == 'Личные расходы':
        cell_amount = list_of_hashes.cell(7, f'{i}').value
        if cell_amount == None:
            self_pay_info()
        elif cell_amount != 0:
            self_pay_info_add_next()
    elif message.text == 'Отложить':
        cell_amount = list_of_hashes.cell(8, f'{i}').value
        if cell_amount == None:
            saving_info()
        elif cell_amount != 0:
            saving_info_add_next()
    elif message.text == 'Сколько осталось':
        how_much_ramains(message)
def how_much_ramains(message):
    cell_amount = list_of_hashes.cell(15, f'{i}').value
    bot.send_message(message.chat.id, cell_amount)
    list_message(message)
def product_info(message):
    bot.send_message(message.chat.id, 'Что мы потратили сегодня на продукты:')
    bot.register_next_step_handler(message, add_info_cell_1)
def add_info_cell_1(message):
    amount = int(message.text)
    list_of_hashes.update_cell( 2, f'{i}', f'{amount}')
    cell_info = list_of_hashes.cell(2, 2).value
    bot.send_message(message.chat.id, 'На продукты осталось: ' + cell_info)
    list_message(message)
def product_info_add_next(message):
    bot.send_message(message.chat.id, 'Сколько еще потратили на продукты:')
    bot.register_next_step_handler(message, add_plus_info_cell_1)
def add_plus_info_cell_1(message):
    amount_new = int(message.text)
    cell_amount = int(list_of_hashes.cell(2, f'{i}').value)
    amount_all = amount_new + cell_amount
    list_of_hashes.update_cell(2, f'{i}', f'{amount_all}')
    cell_info = list_of_hashes.cell(2, 2).value
    bot.send_message(message.chat.id, 'На продукты осталось: ' + cell_info)
    list_message(message)
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
bot.polling()
