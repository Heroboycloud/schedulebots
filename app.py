import os,requests
from flask import Flask
from faker import Faker
import telebot,time
from telebot import types
import util
import pyjokes

Token= os.environ.get('Token')
bot= telebot.TeleBot(Token)
fake= Faker()



app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hi, Welcome to Schedulebot site</h1><p>Here is a free joke {pyjokes.get_joke()}</p> "

@app.route('/joke')
def joje_world():
    title= "Daily Dose of Jokes"
    url= "https://v2.jokeapi.dev/joke/Any?format=txt"
    channel_id= os.environ.get('channel_id')
    headers= {"user-agent":fake.user_agent()}
    joke= requests.get(url,headers=headers).text
    joke_1= util.message.format(title,joke)
    bot.send_message(channel_id,joke_1,parse_mode="Markdown")
    return joke

@app.route('/chuck_norris')
def chuck():
    title= "Chuck Norris Jokes"
    url= "https://api.chucknorris.io/jokes/random"
    channel_id= os.environ.get('channel_id')
    headers= {"user-agent":fake.user_agent()}
    joke= requests.get(url,headers=headers).json()
    joke_1= util.message.format(title,joke["value"])
    bot.send_message(channel_id,joke_1,parse_mode="Markdown")
    return joke




@app.route('/pro_joke')
def program_joke():
    title= "Daily Dose of Jokes"
    joke= pyjokes.get_joke()
    joke_1= util.message.format(title,joke)
    bot.send_message(channel_id,joke_1,parse_mode="Markdown")
    return joke
