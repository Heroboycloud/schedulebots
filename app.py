import os,requests
from flask import Flask
from faker import Faker
import telebot,time
from telebot import types

Token= os.environ.get('Token')
bot= telebot.TeleBot(Token)
fake= Faker()



app = Flask(__name__)

@app.route('/joke')
def hello_world():
    url= "https://v2.jokeapi.dev/joke/Any?format=txt"
    channel_id= os.environ.get('channel_id')
    headers= {"user-agent":fake.user_agent()}
    joke= requests.get(url,headers=headers).text
    bot.send_message(channel_id,joke)
    return joke

@app.route('/chuck_norris')
def chuck():
    url= "https://api.chucknorris.io/jokes/random"
    channel_id= os.environ.get('channel_id')
    headers= {"user-agent":fake.user_agent()}
    joke= requests.get(url,headers=headers).json()
    bot.send_message(channel_id,joke["value"])
    return joke
