from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
TOKEN = "7442265909:AAF2LKHNTp-w9hJ9JUtdwNybeI2To2QLqxc"
from aiogram.utils import executor
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
from model import *

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Я бот. Приятно познакомиться, {msg.from_user.first_name}')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
   else:
       await msg.answer('Не понимаю, что это значит.')

@dp.message_handler(commands=['recognize'], content_types=['photo'])
async def recognize():
    detect_apocalypse()
    

if __name__ == '__main__':
   executor.start_polling(dp)