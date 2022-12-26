
import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("Ok")


async def order_pizza():
    await bot.send_message(chat_id=chat_id, text="Закажи пиццу!")


async def scheduler():
    aioschedule.every().tuesday.at("1:00").do(order_pizza)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)