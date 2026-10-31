import telebot

# ВСТАВЬ СВОЙ НОВЫЙ ТОКЕН МЕЖДУ КАВЫЧКАМИ!
TOKEN = '9297058278:AAFh_9XrlQxa5VBYc0IOe8YS6Kqh_myo2m4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Я твой первый бот. Я работаю!")

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, "Я получил твое сообщение, но пока не умею решать задачи. Скоро научусь!")

print("Бот запущен! Иди в Telegram на телефоне и напиши ему.")
bot.infinity_polling()