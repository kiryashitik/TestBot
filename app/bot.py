import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

bot = Bot(token=os.getenv("8252785543:AAFjc_rvmMhZqsqllX3uhP0XDHmwOTuqURA"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Бот работает на Render!")

async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_bot())