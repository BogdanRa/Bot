import telebot
from sqllite import *

bot = telebot.TeleBot('916963407:AAFWeXoD5jfDeselQXaB7fvFs9kNs7HfY1w')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('links', 'bye')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hey you pull me /start', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def return_links(message):
    print message.chat.id
    print "------------"
    print message.text
    if 'http' or 'https' in message.text:
        appendlinks(message.chat.id, message.text)

    if message.text == "links":

        #bot.send_message(message.chat.id, '\n'.join(BD)+'\n')
        bot.send_message(message.chat.id, execute(message.chat.id))
        print (message.chat.id)





bot.polling(none_stop=True, interval=0)