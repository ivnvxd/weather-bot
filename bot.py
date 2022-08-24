import logging
from aiogram import Bot, Dispatcher, executor, types
import coordinates

import config

API_TOKEN = config.BOT_API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode="html")
dp = Dispatcher(bot)


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    button = types.KeyboardButton("Share Position", request_location=True)
    keyboard.add(button)
    return keyboard


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    coordinates.get_coordinates(lat, lon)
    await message.answer(reply, reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['locate_me'])
async def cmd_locate_me(message: types.Message):
    reply = "Click on the the button below to share your location"
    await message.answer(reply, reply_markup=get_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)