from aiogram.types import InlineKeyboardButton,\
    InlineKeyboardMarkup, CallbackQuery
from aiogram import Dispatcher, bot
from config import bot

async def quiz_2(call: CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question ='Какого номинала "GeekCoin" не бывает?'
    answers = [
        '150 с',
        '350 с',
        '400 c'
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Чеееееееееееееееееел...\n'
                    '(правильный ответ: 400 c)',
        reply_markup=markup
    )

async def quiz_3(call: CallbackQuery):
    question ='Кто оснаватели GeekTech'
    answers = [
        'Сулайманов Нургазы',
        'Айдар Бакиров',
        'они оба'
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Чеееееееееееееееееел...\n'
                    '(правильный ответ: оба)'
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")