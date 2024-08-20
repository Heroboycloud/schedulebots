import os,requests
from flask import Flask
import telebot,time
from telebot import types

Token= os.environ.get('Token')
bot= telebot.TeleBot(Token)




app = Flask(__name__)

@app.route('/joke')
def hello_world():
    url= "https://v2.jokeapi.dev/joke/Any?format=txt"
    channel_id= ""
    joke= requests.get(url).text
    bot.send_message(channel_id,joke)
    return joke

