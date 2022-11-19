import asyncio
import pprint

import aioschedule
from config import BOT_TOKEN, CHANNEL_ID, IP
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor
from ping import is_ping_available, AccessibilityCheck

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['ping'])
async def try_ping_my_router(message: types.Message):
    if is_ping_available(IP):
        await bot.send_message(CHANNEL_ID, 'now u can work')
    else:
        await bot.send_message(CHANNEL_ID, 'now u cant work, loh')


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    await msg.reply('без поняття як на таке реагувати(')


async def scheduler():
    ac = AccessibilityCheck(bot, CHANNEL_ID)
    await ac.checking(IP)

async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
