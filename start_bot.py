from handlers import client, callback, extra,\
     admin, fsm_anketa, notification
from database.bot_db import sql_create
from aiogram.utils import executor
from config import dp
import asyncio
import logging


client.register_handler_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_anketa.register_handlers_fsm_anketa(dp)
notification.register_handlers_notification(dp)


async def on_starup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_starup)