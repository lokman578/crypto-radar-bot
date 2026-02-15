
import telebot

TOKEN = 8516046007:AAGQuDM5FY16mIkk9jFXfdb4yVZSkPYbDcQ

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🚀 Crypto Radar Bot Aktif!")

bot.infinity_polling()
