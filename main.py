import os
import telebot
import time
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('api')
bot = telebot.TeleBot(API_KEY)

def findat(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=["Start"])
def start(message):
    bot.send_message(message.chat.id, "Hya, Greetings !!\nType Help")

@bot.message_handler(commands=["Hello"])
def hello(message):
    bot.send_message(message.chat.id, "I'm God, Just Saying !!")

@bot.message_handler(commands=["Help"])
def help(message):
    bot.send_message(message.chat.id, "Type @instagram_user, I'll create hyperlink for you")

@bot.message_handler(commands=["Wassup"])
def wassup(message):
    bot.send_message(message.chat.id, "I am Good, How you?")

@bot.message_handler(func= lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text =findat(texts)

    bot.send_message(message.chat.id,'https://instagram.com/{}'.format(at_text[1:]))

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(5)

