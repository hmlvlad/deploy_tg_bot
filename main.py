import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os

token = '8148038141:AAG-na4ihqNcPl4R8XS3gUcmWLJuxkrT210'
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello Dimon!")

@dp.message()
async def send_doc(message):
    await message.reply('Успешно')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
