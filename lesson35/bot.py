import telebot
from telebot import types

from datetime import datetime, timedelta, time
from date_time_event import Untiltime

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

start = ''
week = ''
stop = ''
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привіт, як самопочуття?")
        bot.register_next_step_handler(message, get_name) 
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/week':
        bot.send_message(message.from_user.id, "Твоє самопочуття за тиждень?")
        bot.register_next_step_handler(message, get_name, get_week) 
    else:
        bot.send_message(message.from_user.id, 'Напиши /week')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "До зустрічі!")
        bot.register_next_step_handler(message, get_name)
        bot.stop_bot()
    else:
        bot.send_message(message.from_user.id, 'Напиши /stop')

def get_name(message):
    global start
    start = message.text
    bot.send_message(message.from_user.id, 'Подивишся дані за тиждень?')
    bot.register_next_step_handler(message, get_week)

def get_week(message):
    global week
    week = message.text
    bot.send_message('Твої дані за тиждень')
    bot.register_next_step_handler(message, get_stop)

def get_stop(message):
    global stop
    bot.send_message(message.from_user.id, 'До зустрічі')
    bot.stop_bot()


bot.polling()
