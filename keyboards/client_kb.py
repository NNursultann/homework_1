from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)

quiz_button = KeyboardButton('/quiz')
mem_button = KeyboardButton('/mem')

start_markup.add(quiz_button, mem_button)