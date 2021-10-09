from random import choice
import random
from key import TOKEN
import telebot


API_KEY = TOKEN
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["Greet"])
def greet(message):
    bot.reply_to(message,"Too much peimn these days")
    

@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id,f"Hello there, {message.text}")

def freereply(message):
    request = message.text.split()
    if request[0] == "bored" :
        return True
    else:
        return False


@bot.message_handler(func=freereply)
def show(message):
    bot.reply_to(message,"""Let's play a game :-),
                            1. Rock  
                            2. Paper 
                            3. Scissor
    please use \ commands while giving your choice""")

@bot.message_handler(commands=["Rock","Paper","Scissors"])
def bored(message):
    user_choice= message.text.split('/')[1]
    options=("Rock","Paper","Scissors")
    choice= random.choice(options)

    if user_choice == choice :
        bot.reply_to(message,f"It's a draw,\n Your Choice: {user_choice}\n Bot  Chose: {choice}")
    elif (user_choice == "Rock" and choice == "Scissors") or (user_choice == "Paper" and choice == "Rock") or (user_choice == "Scissors" and choice == "Paper"):
        bot.reply_to(message,f"You Have Won,\n Your Choice: {user_choice} \n Bot  Chose: {choice}")
    else:
        bot.reply_to(message,f"Sorry,You Lose,\n Your Choice: {user_choice} \n Bot  Chose: {choice}")


print("it's working")

bot.polling()

