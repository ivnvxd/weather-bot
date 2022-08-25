from os import getenv
from aiogram import Bot, Dispatcher, executor, types
import logging

import messages

import config
API_TOKEN = config.BOT_API_TOKEN
# API_TOKEN = getenv("BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode="html")
dp = Dispatcher(bot)


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("📍 Share Location", request_location=True)
    keyboard.add(button)
    return keyboard


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    reply = messages.weather(message.location.latitude, message.location.longitude)
    await message.answer(text=reply)


@dp.message_handler(commands=['start'])
async def cmd_locate_me(message: types.Message):
    reply = "Click on the button below to share your location"
    await message.answer(reply, reply_markup=get_keyboard())


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply("Type /start to get weather")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)