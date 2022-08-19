import telebot
from telebot import types
import requests
from datetime import date
import json
from config import botoken
bot = telebot.TeleBot(botoken)
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Посмотреть картинку за сегодня")
    btn2 = types.KeyboardButton("Посмотреть картинку за определенный день")
    btn3 = types.KeyboardButton("Посмотреть картинку за определенные дни")
    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    bot.send_message(message.chat.id, text='Выбери что сегодня смотрим.'.format(message.from_user), reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def choice(message):
    if message.text == "Посмотреть картинку за определенный день":
        input_day(message)
    elif message.text == "Посмотреть картинку за определенные дни":
        input_date_from(message)
    elif message.text == "Посмотреть картинку за сегодня":
        today_day(message)
@bot.message_handler(commands=['oneday'])
def input_day(message):
    bot.send_message(message.chat.id, 'Укажите дату поиска (в формате гггг-мм-дд): ')
    bot.register_next_step_handler(message, one_day)
def one_day(message):
    global wrong_date
    wrong_date = 'Неправильно введенная дата'
    try:
        while True:
            date = message.text
            r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal&date={date}')
            parsed = r.json()
            if r.status_code == 200:
                url = parsed['url']
                text = parsed['explanation'] 
                bot.send_photo(message.chat.id, url)
                bot.send_message(message.chat.id, text)
                break 
            elif r.status_code == 400:
                bot.send_message(message.chat.id, 'wrong_date')
                break  
    except ValueError:
        bot.send_message(message.chat.id, 'wrong_date')
    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, err)
    start_message(message)
@bot.message_handler(commands=['severalday'])
def input_date_from(message):
    bot.send_message(message.chat.id, 'Укажите дату первого дня поиска (в формате гггг-мм-дд ): ')
    bot.register_next_step_handler(message, input_date_to)
def input_date_to(message):
    global startdate
    startdate = message.text
    bot.send_message(message.chat.id, 'Укажите дату последнего дня поиска (в формате гггг-мм-дд ): ')
    bot.register_next_step_handler(message, date_from_to)
def date_from_to(message):
    try:   
        while True:      
            enddate = message.text
            r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal&start_date={startdate}&end_date={enddate}')                           
            parsed = r.json()
            if r.status_code == 200:
                for x in parsed:
                    url1 = x['url']
                    text1 = x['explanation']
                    date1 = x['date']
                    bot.send_message(message.chat.id, 'Дата сьемки: '+date1)
                    bot.send_photo(message.chat.id, url1)
                    bot.send_message(message.chat.id, text1)
                break
            elif r.status_code == 400:
               bot.send_message(message.chat.id, 'wrong_date')
               break
    except ValueError:
        bot.send_message(message.chat.id, 'wrong_date')
        input_date_from(message)
    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, err)
    start_message(message) 
@bot.message_handler(commands=['todayday'])
def today_day(message):
    try:
        while True:
            today = str(date.today())
            r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal&date={today}')
            parsed = r.json()
            if r.status_code == 200:
                url = parsed['url']
                text = parsed['explanation'] 
                bot.send_photo(message.chat.id, url)
                bot.send_message(message.chat.id, text)
                break 
    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, err)
        start_message(message)
    start_message(message)
bot.polling()
