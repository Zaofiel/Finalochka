import telebot
from model import *
from spiski import *
import random, os

API_TOKEN = '7442265909:AAF2LKHNTp-w9hJ9JUtdwNybeI2To2QLqxc'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Привет, это катаклизм бот, отправляй мне картинки с апокалиплами от глобального потепления и я угадаю его,
также с помощью команды /facts можно узнать рандомный факт про них
!!!СКАНИРУЮ ТОЛЬКО АПОКАЛИПСЫ ОТ ГЛОБАЛЬНОГО ПОТЕПЛЕНИЯ!!!""")

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    file_id = message.photo[-1].file_id
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(f"{file_id}.jpg", "wb") as new_file:
        new_file.write(downloaded_file)
    name = detect_apocalypse(img = f"{file_id}.jpg", model = 'converted_keras/keras_model.h5', label = 'converted_keras/labels.txt')
    if name.strip() == 'засуха':
        bot.send_message(message.chat.id, f'Это засуха, вот факт про неё {random.choices(drought)}')
    elif name.strip() == 'наводнение':
        bot.send_message(message.chat.id, f'Это наводнение или шторм, вот факт про него  {random.choices(flood)}')
    elif name.strip() == 'коралл':
        bot.send_message(message.chat.id, f'Это коралл, вот факт про него  {random.choices(coral)}')
    elif name.strip() == 'миграция':
        bot.send_message(message.chat.id, f'Это миграция, вот факт про неё  {random.choices(migration)}')
    elif name.strip() == 'вирус':
        bot.send_message(message.chat.id, f'Это вирус, вот факт про него  {random.choices(virus)}')
    else:
        bot.send_message(message.chat.id, 'Мы не распознали изображение')
    os.remove(f"{file_id}.jpg")
    
@bot.message_handler(commands=["facts"])
def facts(message):
    fact = random.choice(all)
    bot.send_message(message.chat.id, fact)
bot.infinity_polling()


