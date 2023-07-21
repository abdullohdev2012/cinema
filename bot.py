import logging
from aiogram import Bot ,Dispatcher ,executor,types
from btn import start_menu,poisk_menu,bak_menu, tart_menu
from keyboards import inline1, informatsiya


logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "5617405325:AAEY5hBxZovPSWBFW4VNKvCby1D8GruwJIQ"

bot = Bot(token=BOT_TOKEN,parse_mode="html")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start_bot(message:types.Message):
    b = await start_menu()
    await message.answer(""" 
    <b>Приветствую тебя в нашем кинотеатре!</b>
    
Популярные фильмы, новинки, сериалы ищите здесь 😉

🌀 Зеркало бота: @ActualMirrorBot

🤟 Приятного использования!
    """, reply_markup=b)

    
@dp.message_handler(text=["🔍поиск"])
async def start_bot(message:types.Message):
    с = await poisk_menu()
    await message.answer(""" 
🔍 Какой фильм или сериал будем искать?
Ищем:<i> по названию </i>
    """, reply_markup=с)

@dp.message_handler(text=["🔙назад"])
async def start_bot(message:types.Message):
    b = await start_menu()
    await message.answer(""" 
    Вы находитесь в главном меню
    """, reply_markup=b)

    


@dp.message_handler(text=["🔥популярное"])
async def start_bot(message:types.Message):
    await message.answer(""" 
1) Волк с Уолл-стрит (2013)
КП: 7.90 | IMDb: 8.20 | биография | 03:00

2) Джордж Форман: Несокрушимый (2023)
КП: 0.00 | IMDb: 6.60 | биография | 02:09

3) Стражи Галактики. Часть 3 (2023)
КП: 8.40 | IMDb: 8.30 | боевик | 02:30

4) Крид 3 (2023)
КП: 6.90 | IMDb: 7.30 | драма | 01:56

5) Форсаж 9 (2021)
КП: 7.90 | IMDb: 8.10 | боевик | 02:25
    """, reply_markup=inline1)    


@dp.message_handler(text=["📼фильмы"])
async def start_bot(message:types.Message):
    await message.answer(""" 
   Выберите раздел
    """, reply_markup=tart_menu)

@dp.message_handler(text=["🗂 Сериалы"])
async def start_bot(message:types.Message):
    await message.answer(""" 
   Выберите раздел
    """, reply_markup=tart_menu)


@dp.message_handler(text=["⭐закладки"])
async def start_bot(message:types.Message):
    b = await bak_menu()
    await message.answer(""" 
   Выберите раздел
    """, reply_markup=b)

@dp.message_handler(text=["👨‍💻 Информация"])
async def start_bot(message:types.Message):
 await message.answer(""" 
  💻 Зеркало бота: @ActualMirrorBot

💎 Продлить/купить подписку: @EasyPayRo_bot

Твой PREMIUM: отсутствует ☹️
    """, reply_markup=informatsiya)


if __name__ == "__main__":
    executor.start_polling(dp)