import random
import telebot
from key import TOKEN
import time

from telebot.types import MessageID

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


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["about"])
def about(message):
    bot.reply_to(message,f"""This is a multi purpose Bot that is still in Development ,\nThis Bot is created from Python,\nAs the Description reads new feature will be added as they are learnt ,\nThank you Kind User :{message.chat.username} for testing  """)
   

@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(message.chat.id,f"Hello there,Kind User😁,\n{message.from_user.first_name}")


#----------------------------------------------keyword for mini games-------------------------------------------------------------------

def freereply(message):
    request = message.text.split()
                
    
    if request[0].lower() == "bored" :                        #test message for RPS
        return True
    else:
        return False

#----------------------------------------------Rock,paper,Scissor-------------------------------------------------------------------

@bot.message_handler(func=freereply)
def show(message):
    bot.reply_to(message,"""Let's play a game :-),
                            1. rock  
                            2. paper 
                            3. scissor
    please use / commands while giving your choice""")

@bot.message_handler(commands=["rock","paper","scissors"])
def bored(message):
    user_choice= message.text.split('/')[1]
    options=("rock","paper","scissors")
    choice= random.choice(options)

    if user_choice == choice :
        bot.reply_to(message,f"It's a draw,\n Your Choice: {user_choice.capitalize()}\n Bot  Chose: {choice.capitalize()}")
    elif (user_choice == "rock" and choice == "scissors") or (user_choice == "paper" and choice == "rock") or (user_choice == "scissors" and choice == "paper"):
        bot.reply_to(message,f"You Have Won,\n Your Choice: {user_choice.capitalize()} \n Bot  Chose: {choice.capitalize()}")
    else:
        bot.reply_to(message,f"Sorry,You Lose,\n Your Choice: {user_choice.capitalize()} \n Bot  Chose: {choice.capitalize()}")

#----------------------------------------------flip a coin-------------------------------------------------------------------
@bot.message_handler(commands=["toss"])
def toss(message):
    sides=("Head","Tail")
    result = random.choice(sides)
#----------------------------------------------8 ball-------------------------------------------------------------------

@bot.message_handler(commands = ["8ball"])
def eightball(message):
  bot.reply_to(message,random.choice(responses))

#----------------------------------------------Auto Memory Doll-------------------------------------------------------------------
@bot.message_handler(commands= ["letter"])
def create_letter(message):
    bot.reply_to(message,"""This will create a formal letter based on your request,
    please follow the mentioned format
    1.From: and ;at the end
    2.To: ;at the end
    3.Subject: ;at the end
    4.days:""")

def heading(message):
    header = message.text.split(":")
    if header[0] == "From":                        
        return True
    else:
        return False

@bot.message_handler(func=heading)
def from_ad(message):
    from_ad = message.text
    vals=from_ad.split(";",3)
    sender_ad =vals[0]
    receiver_ad =vals[1]
    sub=vals[2]
    way=(f'{sender_ad}\n'
        f'{receiver_ad}\n'
        f'{sub}\n'
         """Dear Mr./Mrs,
            I am writing to request your approval for a 10-day leave for my planned vacation. I would like to take my vacation during the summer from {start date} to {end date} to take a cruise trip through the Bahamas with my wife and kids.
            I feel incredibly confident that the rest of the team should be able to continue excellent work during my absence.
            I look forward to your response and also thank you for your consideration.
                                    Thanking You,                                       """)  
    
    bot.send_message(message.chat.id,way)

#------------------------------------------------END-------------------------------------------------------------------  
print("it's live now")

while True:
    try:
        bot.polling(skip_pending=True)
    except:
        time.sleep(5)

