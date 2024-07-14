import telebot
from telebot.types import *


web_app_url = "https://exemple.com/"

bot = telebot.TeleBot("API_KEY",parse_mode='html')




@bot.message_handler(commands=['start'])
def start_handler(msg):
    bot.reply_to(msg,"<b>O'yini boshlash uchun bosing! 👇</b>",reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Start",web_app=WebAppInfo(web_app_url))))




print("Bot username: @"+bot.get_me().username)
bot.infinity_polling()
