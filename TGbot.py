import telebot
from sqllite import *
from urlpars import parse_url, parse_domain
import time

bot = telebot.TeleBot()


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('habr')
keyboard1.row('xakep')
keyboard1.row('tproger')
keyboard1.row('others')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Send your favorites link here and put /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def append_links(message):
    if parse_url(message.text):

        appendlinks(message.chat.id, message.text, parse_domain(message.text))
        bot.send_message(message.chat.id, "The link has added")

        #add to SQLlight

    #select links from sql
    key_words = ['habr', 'xakep', 'tproger']

    if message.text in key_words:

        for data_links in execute(message.chat.id, message.text):
            bot.send_message(message.chat.id, data_links)
            time.sleep(0.5)

    elif message.text == 'others':
        for data_links in other_excute(message.chat.id):
            bot.send_message(message.chat.id, data_links)
            time.sleep(0.5)

    else:
        pass




bot.polling(none_stop=True, interval=0)