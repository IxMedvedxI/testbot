import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import random
from googletrans import Translator, constants

mas = ['a','b']
mas[0] = 'b'
print(mas)


def fun(st):
  str(st)
  y = "яЯ"
  st.split()
  if y[0] in st or y[1] in st:
    for i in range(len(st)):
      if st[i] == y[0] or st[i] == y[1]:
        st[i] = 'ты' 
  return st

token ='5413641390:AAEcZAElsbwbWXkO6e8Fhwj6RFAHNB2892c'
bot = telebot.TeleBot(token)
translator = Translator()

@bot.message_handler(commands=['start'])
def start_message(message):
  #bot.send_message(message.chat.id,"Привет")
  markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1=types.KeyboardButton("Нажми")
  markup.add(item1)
  bot.send_message(message.chat.id,'Привет!',reply_markup=markup)

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
    else:
      bot.send_message(message.chat.id,fun(message.text))


bot.infinity_polling()
