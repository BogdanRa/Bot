import telebot
bot = telebot.TeleBot('916963407:AAFWeXoD5jfDeselQXaB7fvFs9kNs7HfY1w')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('links', 'bye')
hey = ['gmail.com', 'prnhub.com', 'gooel.com']
BD = []

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hey you pull me /start', reply_markup=keyboard1)

"""""
@bot.message_handler(content_types=['text'])
def storege_message(message):
    #if message.text in 'http':
    BD.append(message.text)
    #else:
    #    pass
    return BD
"""""

@bot.message_handler(content_types=['text'])
def return_links(message):
    if 'http' or 'https' in message.text:
        BD.append(message.text)

    if message.text == "links":

        bot.send_message(message.chat.id, '\n'.join(BD)+'\n')






bot.polling(none_stop=True, interval=0)