from aiogram.types import Message
from aiogram import Dispatcher

async def echo(message: Message):
    try:
     message.text = int(message.text)
     await message.answer(message.text ** 2)
    except ValueError:
        await message.answer(message.text)

def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)