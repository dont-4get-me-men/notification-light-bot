import asyncio
import pprint

import aioschedule
from config import BOT_TOKEN, CHANNEL_ID
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)

def exemle():
    pass

async def process_do_it_4_all(message: types.Message):
    pprint.pprint(message)
    a = 12
    await message.reply()

@dp.message_handler(commands=['ping'])
async def process_do_it_4_all(message: types.Message):
    await bot.send_message(CHANNEL_ID, 'ok')

@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    await msg.reply('без поняття як на таке реагувати(')


async def send_4_all():
    await bot.send_message(CHANNEL_ID, " lol")


async def scheduler():
    aioschedule.every().day.at("9:00").do(send_4_all)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
