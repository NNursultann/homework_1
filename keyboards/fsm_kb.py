from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_button = KeyboardButton('CANCEL')
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

backend = KeyboardButton("BACKEND")
frontend = KeyboardButton("FRONTEND")
ux_ui = KeyboardButton("UX/UI")
android = KeyboardButton("ANDROID")
ios = KeyboardButton("IOS")

direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(backend, frontend, ux_ui, android, ios, cancel_button)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('ДА'), KeyboardButton('НЕТ'))
