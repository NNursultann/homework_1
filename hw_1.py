import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message


TOKEN ='5638949458:AAHfn_1YzjKDVy4izuhG-rtW1-ualfegdgU'

logging.basicConfig(level=logging.INFO)

bot =Bot(token=TOKEN)
dispat =Dispatcher(bot)




@dispat.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.answer(f'вас приветствует HomeWork #1 \n'
                         f'что-бы узнать доступные команды напишите /help')

@dispat.message_handler(commands=['help'])
async def send_help_welcome(message: Message):
    await message.answer('вызвали команду help!\n'
                        'Доступные для вас команды:\n'
                        '/my_info - выводит инфу о вас\n'
                        '/download_photo - скачивает вашу аватарку\n'
                        '/show_movies - список фильмов\n'
                        '/send_my_info - пользователь пишет свое имя,'
                         ' фамилия, возраст, чем занимается '
                         'и список любимых фильмов или сериалов '
                         'и бот группирует это в таком сообщении \n')

@dispat.message_handler(commands=['my_info'])
async def my_info(message: Message):
    await message.reply(f'имя:{message.from_user.first_name} '
                        f'{message.from_user.last_name}\n'
                        f'id: {message.from_id}')


@dispat.message_handler(commands=['download_photo'])
async def downld_avatar(message):

    await bot.get_user_profile_photos(message.from_user.id)
    profile_pictures = await dispat.bot.get_user_profile_photos(message.from_user.id)
    await message.answer_photo(dict((profile_pictures.photos[0][0])).get("file_id"))

@dispat.message_handler(commands=['show_movies'])
async def movies_(message: Message):
    await message.reply(f'фильмы для вас:\n'
                        f'Человек-паук: Нет пути домой - '
                        f'https://kinogo.pub/32242-chelovek-pauk-net-puti-domoj-2021-v3.html \n\n '
                        f'Мой сосед Тоторо - https://kinoprofi.vip/3467-moy-sosed-totoro-2008.html \n\n'
                        f'Пираты Карибского моря: Проклятие Черной жемчужины'
                        f' - https://gidonline.io/film/piraty-karibskogo-morya-proklyatie-chernoj-zhemchuzhiny/ \n\n'
                        f'Шерлок - https://sherlock-online.ru/ \n\n'
                        f'Гарри Поттер и философский камень -'
                        f' https://kinogo.pub/252-film-garri-potter-i-filosofskij-kamen.html \n\n'
                        f'вскором времени добавим ещё фильмов))')

@dispat.message_handler(commands=['send_my_info'])
async def my_info(message: Message):
    personal_info = (message.text).split(sep="\n")
    name = personal_info[1:2]
    surname = personal_info[2:3]
    age = personal_info[3:4]
    hobby = personal_info[4:5]
    fav_movies_list = personal_info[5:]
    await message.answer(f'1.ваше имя {name} {surname}\n'
                        f'2.ваш возраст {age}\n'
                        f'3.вы занимаетесь {hobby}\n'
                        f'4.ваши любимые фильмы и сериалы {fav_movies_list}')



executor.start_polling(dispat,skip_updates=True)


