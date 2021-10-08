import telebot

API_KEY = "TOKEN"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["Greet"])
def greet(message):
    bot.reply_to(message,"hey i hopes this works!!!")

bot.polling()
