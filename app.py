import os
import threading
from flask import Flask
import telebot

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я твой первый бот. Я работаю!")

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, "Я получил твое сообщение, но пока не умею решать задачи. Скоро научусь!")

def run_bot():
    bot.infinity_polling()

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)