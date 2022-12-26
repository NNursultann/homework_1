from aiogram.types import Message
from aiogram import Dispatcher
from config import ADMINS
from random import choice

async def game_(msg: Message):
    games = ['🎲', '🎳', '🎰', '🏀', '⚽️', '🎯']
    if msg.text.startswith('game'):
        if msg.chat.type != 'private':
            if msg.from_user.id not in ADMINS:
                 await msg.answer("Кто ты? Ты не админ!")
            else:
               await msg.answer_dice(emoji=choice(games))
        else:
            await msg.answer('Пиши в группе!!')

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game_,
                                lambda word: 'game' in word.text)