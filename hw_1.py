from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message
from decouple import config
import random
import logging
TOKEN =config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

logging.basicConfig(level=logging.INFO)
@dp.message_handler(commands=['start','help'])
async def start_bot(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}\n'
                         f'Интересные команды:\n'
                         f'/quiz - викторина\n'
                         f'/mem - отправляет мем')

@dp.message_handler(commands=['quiz'])
async def quiz_(message:Message):
    question ='Когда открылся первый филиал "GeekTech"?'
    answers = [
        'в 2016',
        'в 2018'
    ]
    await message.answer_poll(
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Чеееееееееееееееееел...\n'
                    '(правильный ответ 2018)'
    )

@dp.message_handler(commands=['mem'])
async def send_mem(message: Message):
    mem1 = open('media/mem_1.jpg', 'rb')
    mem2 = open('media/mem_2.jpg', 'rb')
    mem3 = open('media/mem_3.jpg', 'rb')
    mems = [mem1, mem2, mem3]
    await message.answer_photo(photo=random.choice(mems))

@dp.message_handler()
async def echo(message: Message):
    try:
     message.text = int(message.text)
     await message.answer(message.text ** 2)
    except ValueError:
        await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)