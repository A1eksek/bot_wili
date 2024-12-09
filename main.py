from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

api = "7984357790:AAHMp_mrKHdNUU6A7kngMUqBvegTURcw9oI"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# kb = ReplyKeyboardMarkup()
# button = KeyboardButton(text='info')
# kb.add(button)

# kb = KeyboardButton()
start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='info')],
        [
            KeyboardButton(text='shop'),
            KeyboardButton(text='donate'),
        ]
    ], resize_keyboard=True
)


@dp.message_handler(commands=['start'])
async def all(message):
    await message.answer("Привет!", reply_markup=start_menu)


@dp.message_handler(text='info')
async def ingo(message):
    await message.answer("Информация о боте")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
