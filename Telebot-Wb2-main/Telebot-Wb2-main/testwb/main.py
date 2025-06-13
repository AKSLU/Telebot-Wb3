import telebot
import requests
from wb import *

token = "7712321312:AAGTEOW2Yfe1vBFe4s1WpdKN4rr8qn_oEwM"
bot = telebot.TeleBot(token)


whitelist = [6685845705]


def bool_login(chat_id):
    return chat_id in whitelist 


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if bool_login(message.chat.id):
        bot.reply_to(message, f"Ваш ID: {message.chat.id}")
    else:
        bot.reply_to(message, "Нет доступа")


@bot.message_handler(commands=['info'])
def send_info(message):
    if bool_login(message.chat.id):
        art = "5007120" 
        url = f"https://basket-01.wbbasket.ru/vol50/part5007/{art}/info/ru/card.json"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "referer": f"https://global.wildberries.ru/catalog/{art}/detail.aspx"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            name = data.get("imt_name", "Название не найдено")
            bot.reply_to(message, name)
        else:
            bot.reply_to(message, f"Ошибка: код {response.status_code}")
    else:
        bot.reply_to(message, "Нет доступа")

@bot.message_handler(commands=['price'])        
def analyze_price(message):
     if bool_login(message.chat.id):
        art = "5007120" 
        url = f"https://basket-05.wbbasket.ru/vol816/part81699/81699980/info/price-history.json"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "referer": f"https://global.wildberries.ru/catalog/{art}/detail.aspx"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            name = data.get("imt_name", "Название не найдено")
            dt =  data.get("dt", "Название не найдено")
            price =  data.get("price", "Название не найдено")
            bot.reply_to(message, name+dt+price)
            #if tek_price > meduim_price:
                #bot.reply_to(message, "Покупать невыгодно: цена выше средней")
            #elif tek_price < meduim_price:
                #bot.reply_to(message, "Покупать выгодно: цена ниже средней")
            #else:
                #bot.reply_to(message, "Нейтрально цена: соответствует средней")
    
bot.polling()

