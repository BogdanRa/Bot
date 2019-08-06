import telebot
from sqllite import *
from urlpars import parse_url

bot = telebot.TeleBot('916963407:AAFWeXoD5jfDeselQXaB7fvFs9kNs7HfY1w')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('habr')
keyboard1.row('xakep')
keyboard1.row('tproger')
keyboard1.row('others')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hey you pull me /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def append_links(message):
    if parse_url(message.text):

        appendlinks(message.chat.id, message.text, parse_domain(message.text))
        #add to SQLlight


    key_words = ['habr', 'xakep', 'tproger']
    print(message.text)
    if message.text in key_words:
        BD = []

        for i in execute(message.chat.id, message.text):

            BD.append(i)
        bot.send_message(message.chat.id, '\n'.join(BD)+'\n')

    else:
        pass




bot.polling(none_stop=True, interval=0)