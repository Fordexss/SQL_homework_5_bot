from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("add_user", "вивисти довідку команд"),
            types.BotCommand("get_users", "вивисти довідку команд"),
        ]
    )
