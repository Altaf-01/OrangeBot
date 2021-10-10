from random import choice
import random
from key import TOKEN
import telebot

responses = [
"It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]

API_KEY = TOKEN

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["about"])
def about(message):
    bot.reply_to(message,f"""This is a multi purpose Bot that is still in Development ,\nThis Bot is created from Python,\nAs the Description reads new feature will be added as they are learnt ,\nThank you Kind User :{message.chat.username} for testing  """)
   

@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(message.chat.id,f"Hello there,Kind User😁,\n{message.chat.username}")

def freereply(message):
    request = message.text.split()
    if request[0] == "bored" :                        #test message for RPS
        return True
    else:
        return False


@bot.message_handler(func=freereply)
def show(message):
    bot.reply_to(message,"""Let's play a game :-),
                            1. rock  
                            2. paper 
                            3. scissor
    please use \ commands while giving your choice""")

@bot.message_handler(commands=["rock","paper","scissors"])
def bored(message):
    user_choice= message.text.split('/')[1]
    options=("rock","paper","scissors")
    choice= random.choice(options)

    if user_choice == choice :
        bot.reply_to(message,f"It's a draw,\n Your Choice: {user_choice}\n Bot  Chose: {choice}")
    elif (user_choice == "rock" and choice == "scissors") or (user_choice == "paper" and choice == "rock") or (user_choice == "scissors" and choice == "paper"):
        bot.reply_to(message,f"You Have Won,\n Your Choice: {user_choice} \n Bot  Chose: {choice}")
    else:
        bot.reply_to(message,f"Sorry,You Lose,\n Your Choice: {user_choice} \n Bot  Chose: {choice}")

#toss a coin
@bot.message_handler(commands=["toss"])
def toss(message):
    sides=("Head","Tail")
    result = random.choice(sides)
    bot.reply_to(message,f"Coin flipped to Give: {result}")

#8ball

@bot.message_handler(commands = ["8ball"])
def eightball(message):
  bot.reply_to(message,random.choice(responses))

    
print("it's working")
bot.polling()

