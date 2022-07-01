import telebot
import requests
bot = telebot.TeleBot('5542226206:AAETwbHXtcWdQS0VoNLT9wjprqv_feu4Log')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Say hello')
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
bot.polling()
