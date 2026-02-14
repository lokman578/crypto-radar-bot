
import telebot

TOKEN = "BURAYA_TOKEN_YAZ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 Crypto Radar Bot Aktif!")

bot.infinity_polling()
