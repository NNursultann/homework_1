from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("TOKEN")
ADMINS = [1703737956]

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)