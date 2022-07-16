from email import message
import telebot
from telebot import types
import json
import random
bot = telebot.TeleBot('5542226206:AAETwbHXtcWdQS0VoNLT9wjprqv_feu4Log')
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать случайный рецепт")
    btn2 = types.KeyboardButton("Выбрать рецепт по ингридиентам")
    btn3 = types.KeyboardButton("Выбрать рецепт по названию блюда")
    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    bot.send_message(message.chat.id, text='Выбери как найти твой рецепт.'.format(message.from_user), reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def choice(message):
    if message.text == "Выбрать случайный рецепт":
        get_random_recipe(message)
    elif message.text == "Выбрать рецепт по ингридиентам":
        get_ingridients(message)
    elif message.text == "Выбрать рецепт по названию блюда":
        get_text_input_from_user(message)
@bot.message_handler(commands=['random'])
def get_random_recipe(message):
    path_data = 'C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json'
    rand = random.randrange(0,3475)
    with open(path_data,'r', encoding='utf-8' ) as file:
        text = json.load(file)
        first_dict = text[rand]
        id_foto = first_dict[0]
        title = first_dict[1]
        body = first_dict[2]
        recipi = first_dict[3]
        url = first_dict[4]
        end = '\n'
    pathimg = (f'C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Картинки\\{id_foto}.jpeg')
    bot.send_photo(message.chat.id, photo=open(pathimg, 'rb'))
    bot.send_message(message.chat.id, title+end+body+end+'Список ингридиентов: '+recipi+end+'Ссылка на рецепт: '+url)
    start_message(message)
@bot.message_handler(commands=['find'])
def get_ingridients(message):
        bot.send_message(message.chat.id, 'Введите ингредиенты: ')
        bot.register_next_step_handler(message, get_specific_recipe)
def get_specific_recipe(message):
    path_data = 'C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json'
    with open(path_data,'r', encoding='utf-8' ) as file:
        text = json.load(file)
        random.shuffle(text)
        string2=str(message.text)
        for i in text:
            id_foto = i[0]
            title = i[1]
            body = i[2]
            url = i[4]
            end = '\n'
            recipi1 = i[3]            
            string1 = recipi1
            unwanted_characters = ".,!?"
            string1_words = set(string1.split())
            string2_words = set(string2.split())
            string1_words = {word.strip(unwanted_characters) for word in string1_words}
            string2_words = {word.strip(unwanted_characters) for word in string2_words}
            string2_words = {word.strip(unwanted_characters).lower() for word in string2_words}
            common_words = string1_words & string2_words
            if len(common_words) >= 3:
                pathimg = (f'C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Картинки\\{id_foto}.jpeg')
                bot.send_photo(message.chat.id, photo=open(pathimg, 'rb'))
                bot.send_message(message.chat.id, title+end+body+end+'Список ингридиентов: '+recipi1+end+'Ссылка на рецепт: '+url)
                break
    start_message(message)
@bot.message_handler(commands=['find_title'])
def get_text_input_from_user(message):
    answer1 = bot.send_message(message.chat.id, 'Введите название блюда по которому будем искать: ')
    bot.register_next_step_handler(answer1, get_number_input_from_user)
def get_number_input_from_user(message):
    global string2
    string2=str(message.text)
    answer2 = bot.send_message(message.chat.id, 'Сколько показывать рецептов: ')
    bot.register_next_step_handler(answer2, get_recipe_by_title)
def get_recipe_by_title(message):
    path_data = 'C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json'
    with open(path_data,'r', encoding='utf-8' ) as file:
        text = json.load(file)
        random.shuffle(text)
        recipe_shown = int(message.text)
        recipe_count = 0
        for i in text:
            id_foto = i[0]
            body = i[2]
            recipi1 = i[3]
            url = i[4]
            end = '\n'
            title = i[1]           
            string1 = title
            unwanted_characters = ".,!?"
            string1_words = set(string1.split())
            string2_words = set(string2.split())
            string1_words = {word.strip(unwanted_characters) for word in string1_words}
            string2_words = {word.strip(unwanted_characters) for word in string2_words}
            string2_words = {word.strip(unwanted_characters).lower() for word in string2_words}
            common_words = string1_words & string2_words
            if len(common_words) >= 1:
                recipe_count +=1
                pathimg = (f'C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Картинки\\{id_foto}.jpeg')
                bot.send_photo(message.chat.id, photo=open(pathimg, 'rb'))
                bot.send_message(message.chat.id, title+end+body+end+'Список ингридиентов: '+recipi1+end+'Ссылка на рецепт: '+url)
                if recipe_shown == recipe_count:
                    break
    start_message(message)
bot.polling()

