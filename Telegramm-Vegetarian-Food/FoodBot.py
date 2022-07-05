from email import message
import telebot
import json
import random
bot = telebot.TeleBot('5542226206:AAETwbHXtcWdQS0VoNLT9wjprqv_feu4Log')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Please print: /random to get a recipe')
@bot.message_handler(commands=['random'])
def get_recipe(message):
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
        bot.send_message(message.chat.id, title+end+body+end+'Список ингридиентов: '+recipi+end+'Ссылка на рецепт: '+url)
    pathimg = (f'C:\\Users\\Aleksey\\Desktop\\База данных вегеторианских рецептов\\Картинки\\{id_foto}.jpeg')
    bot.send_photo(message.chat.id, photo=open(pathimg, 'rb'))
bot.polling()
