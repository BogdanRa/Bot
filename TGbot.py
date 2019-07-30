import telebot
bot = telebot.TeleBot('916963407:AAFWeXoD5jfDeselQXaB7fvFs9kNs7HfY1w')

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "hello":
        bot.send_message(message.from_user.id, "Hello how can I help you?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "say hello")
    else:
        bot.send_message(message.from_user.id, "I don't... unders.. you.. w /help.")



bot.polling(none_stop=True, interval=0)