import telebot

API_KEY = "2071211745:AAHxYbvOQWy37TtlRa2B7WBFjo7n4Uy2vC8"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["Greet"])
def greet(message):
    bot.reply_to(message,"hey i hopes this works!!!")

bot.polling()
