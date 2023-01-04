from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from decouple import config

fsmcontext_proxy_storage = MemoryStorage()

TOKEN = config("TOKEN")
ADMINS = [1703737956]

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=fsmcontext_proxy_storage)