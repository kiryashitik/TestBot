import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Бот работает!")

async def run():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())