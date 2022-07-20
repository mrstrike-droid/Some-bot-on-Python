import telebot
from telebot import types
import requests
import json
bot = telebot.TeleBot('5558566177:AAHpNimakvw3qU-ur3hAuZFw6XHuAEy-nD8')
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Посмотреть картинку за день")
    btn2 = types.KeyboardButton("Посмотреть картинку за определенные дни")
    keyboard.add(btn1)
    keyboard.add(btn2)
    bot.send_message(message.chat.id, text='Выбери что сегодня смотрим.'.format(message.from_user), reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def choice(message):
    if message.text == "Посмотреть картинку за день":
        input_day(message)
    elif message.text == "Посмотреть картинку за определенные дни":
        input_date_from(message)
@bot.message_handler(commands=['oneday'])
def input_day(message):
    bot.send_message(message.chat.id, 'Укажите дату поиска (в формате гггг-мм-дд ): ')
    bot.register_next_step_handler(message, one_day)
def one_day(message):
    try:
        while True:
            date =message.text
            r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=Zex7CBAHQmbVfomUeIOyZXt9d8JccD4R50fNNhal&date={date}')
            parsed = r.json()
            if r.status_code == 200:
                url = parsed['url']
                text = parsed['explanation'] 
                bot.send_photo(message.chat.id, url)
                bot.send_message(message.chat.id, text)
                break 
            elif r.status_code == 400:
                print ('Wrong date format')                               
    except ValueError:
        print('Please enter: 1 or 2')
    except requests.exceptions.HTTPError as err:
        print (err)
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
                print ('Wrong date format')
    except ValueError:
        print('Please enter: 1 or 2')
    except requests.exceptions.HTTPError as err:
        print (err)
    start_message(message)                  
bot.polling()
