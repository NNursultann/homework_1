from aiogram.types import Message, InlineKeyboardButton,\
    InlineKeyboardMarkup
from keyboards.client_kb import start_markup
from aiogram import Dispatcher
from config import bot
from parser.wheels import ParserWheels
import random

async def start_bot(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}\n'
                         f'Интересные команды:\n'
                         f'/quiz - викторина\n'
                         f'/mem - отправляет мем', reply_markup=start_markup)

async def quiz_(message: Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question ='Когда открылся первый филиал "GeekTech"?'
    answers = [
        'в 2016',
        'в 2018',
        'в 2022'
    ]

    await message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Чеееееееееееееееееел...\n'
                    '(правильный ответ: 2018)',
        reply_markup=markup
    )

async def send_mem(message: Message):
    mem1 = open('media/mem_1.jpg', 'rb')
    mem2 = open('media/mem_2.jpg', 'rb')
    mem3 = open('media/mem_3.jpg', 'rb')
    mems = [mem1, mem2, mem3]
    await message.answer_photo(photo=random.choice(mems))

async def pin(msg: Message):
    if msg.reply_to_message:
        await bot.pin_chat_message(msg.chat.id, msg.message_id)

async def get_wheels(message: Message):
    wheels = ParserWheels.parser()
    for i in wheels:
        await message.answer(
            f"{i['link']}\n",
            f"#{i['size']}\n",
            f"#{i['logo']}\n",
            f"{i['price']}"
        )


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(quiz_, commands=['quiz'])
    dp.register_message_handler(send_mem, commands=['mem'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(get_wheels, commands=['wheels'])
