from email import message
import telebot
import json
import random
bot = telebot.TeleBot('5542226206:AAETwbHXtcWdQS0VoNLT9wjprqv_feu4Log')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Напишите: /random что бы получить рандомный рецепт или напишите: /find что бы найти рецепт по ключевым словам')
@bot.message_handler(commands=['random'])
def get_random_recipe(message):
    rand = random.randrange(0,3475)
    with open('C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json','r', encoding='utf-8' ) as file:
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
@bot.message_handler(commands=['find'])
def get_ingridients(message):
        bot.send_message(message.chat.id, 'Введите ингредиенты: ')
        bot.register_next_step_handler(message, get_specific_recipe)
def get_specific_recipe(message):
    with open('C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Recepies.json','r', encoding='utf-8' ) as file:
        text = json.load(file)
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
bot.polling()
