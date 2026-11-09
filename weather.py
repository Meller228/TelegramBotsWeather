import telebot
import requests


TOKEN = 'ТОКЕН'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Напиши название города , и я скажу, какая там погода.")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    try:
        response = requests.get(f'https://wttr.in/{city}?format=3')
        if response.status_code == 200:
            bot.reply_to(message, response.text)
        else:
            bot.reply_to(message, "Город не найден.")
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка. Попробуй позже.")

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()