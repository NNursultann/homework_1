from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.bot_db import sql_command_insert
from keyboards import fsm_kb
from config import ADMINS

class FSMAdmin(StatesGroup):
    id = State()
    full_name = State()
    direction = State()
    age = State()
    group = State()
    contact = State()
    submit = State()

async def fsm_start(message: types.Message):
        if message.chat.type == 'private':
            # if message.from_user.id == ADMINS:
                await FSMAdmin.id.set()
                await message.answer("Id ментора")
            # else:
            #     await message.answer('Кто ты? ТЫ НЕ АДМИН!!!!!!')
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
    await message.answer("Направление ментора", reply_markup=fsm_kb.direction_markup)

async def load_direction(message: types.Message, state: FSMContext):
    if message.text not in ["BACKEND", "FRONTEND", "UX/UI", "ANDROID", "IOS"]:
        await message.answer("Выбери из списка!")
    else:
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
    await message.answer(f"id: {data['id']}\n"
                         f"Имя: {data['full_name']}\n"
                         f"Направление: {data['direction']}\n"
                         f"Возраст: {data['age']}\n"
                         f"Группа: {data['group']}\n"
                         f"Контакт: {data['contact']}\n"
                         )
    await FSMAdmin.next()
    await message.answer("Все верно?", reply_markup=fsm_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Ментор зареган")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Нет, так нет...!")
    else:
        await message.answer('НИПОНЯЛ!?')

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Отмена, так отмена")

def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=['reg_mentors'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.full_name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_contact, state=FSMAdmin.contact)
    dp.register_message_handler(submit, state=FSMAdmin.submit)