import telebot
import psycopg2 as pgsql

BOT_TOKEN = '5860842320:AAEfKtZppebM_04-4yspPqntUhZlmZCv2kg' 
bot = telebot.TeleBot(BOT_TOKEN)




print('Connecting to the PostgreSQL database...')
connection=pgsql.connect(host="localhost", dbname="telebot", user="postgres", 
                         password="damir2004")

cur = connection.cursor()


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello, how are you doing?")

@bot.message_handler(content_types=['photo', 'video'])
def photoVideo(message):
    bot.send_message(message.chat.id, 'Cool')

@bot.message_handler(func=lambda message : True)
def anyMessage(message):
    bot.send_message(message.chat.id, 'I don''t know this command')

  
bot.polling()
