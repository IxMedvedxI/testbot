import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import random
from googletrans import Translator, constants

token ='5413641390:AAEcZAElsbwbWXkO6e8Fhwj6RFAHNB2892c'
bot = telebot.TeleBot(token)
translator = Translator()

@bot.message_handler(commands=['start'])
def start_message(message):
  #bot.send_message(message.chat.id,"Привет")
  markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1=types.KeyboardButton("Нажми")
  markup.add(item1)
  bot.send_message(message.chat.id,'Привет',reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Нажми":
      rd = random.randint(1,10)
      url = "https://quotes.toscrape.com/page/"+str(rd)+"/"
      response = requests.get(url)
      soup = BeautifulSoup(response.text,'lxml')
      quotes = soup.find_all('span',class_='text')
      rd = random.choice(quotes).text
      result = translator.translate(rd,dest = 'ru')
      bot.send_message(message.chat.id,result.text)


bot.infinity_polling()
