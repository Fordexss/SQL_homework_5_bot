import sqlite3

from aiogram import types
from aiogram.types import ParseMode

from loader import dp

with sqlite3.connect('users.db') as db:
    cursor = db.cursor()

    # Створюємо таблицю "users", якщо її не існує
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT
        )
    ''')
    db.commit()


# Тут його логіка тобто додавання до бази
    async def add_user(user: types.User):
        cursor.execute('''
            INSERT INTO users (username, first_name, last_name)
            VALUES (?, ?, ?)
        ''', (user.username, user.first_name, user.last_name))
        db.commit()


    async def get_users():
        cursor.execute('SELECT username, first_name, last_name FROM users')
        users_data = cursor.fetchall()
        return users_data


# Просто відповіді
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привіт! Я бот для роботи з користувачами. Використовуйте команди /add_user і /get_users.")


@dp.message_handler(commands=['add_user'])
async def on_add_user(message: types.Message):
    await add_user(message.from_user)
    await message.reply("Ви були додані до бази даних!")


# Вивід
@dp.message_handler(commands=['get_users'])
async def on_get_users(message: types.Message):
    users_data = await get_users()
    if users_data:
        users_list = "\n".join(
            f"@{username} - {first_name} {last_name}" for username, first_name, last_name in users_data)
        await message.reply(f"Список користувачів:\n{users_list}", parse_mode=ParseMode.MARKDOWN)
    else:
        await message.reply("У базі даних немає користувачів.")
