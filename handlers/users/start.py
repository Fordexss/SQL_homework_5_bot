from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def on_start(message: types.Message):
    await message.answer("Привіт! Я бот рееструвач. Використовуйте команди /add_user і /get_users.")
