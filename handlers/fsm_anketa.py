from aiogram import Dispatcher,types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from config import ADMINS

class FSMAdmin(StatesGroup):
    id = State
    full_name = State
    direction = State
    age = State
    group = State
    contact = State

async def fsm_start(message: types.Message):
        if message.chat.type == 'private':
            await FSMAdmin.id.set()
            await message.answer("Id ментора")
        else:
            await message.answer("Пиши в личке!")

async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    await FSMAdmin.next()
    await message.answer("Фамилие,имя ментора")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['full_name'] = message.text
    await FSMAdmin.next()
    await message.answer("Направление ментора")

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Возраст ментора")

async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа")
    elif int(message.text) < 5 or int(message.text) > 80:
        await message.answer("Возростное ограничение!")
    else:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Группа ментора")

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMAdmin.next()
    await message.answer("Контакт ментора")

async def load_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text
    await state.finish()


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.full_name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_contact, state=FSMAdmin.contact)