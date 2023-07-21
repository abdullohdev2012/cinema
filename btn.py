from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


async def start_menu():
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn.add(
        KeyboardButton("🔍поиск"),
        KeyboardButton("🔥популярное"),
        KeyboardButton("📼фильмы"),
        KeyboardButton("⭐закладки"),
        KeyboardButton("🗂 Сериалы"),
        KeyboardButton("👨‍💻 Информация"),
 
    )
    return btn

async def poisk_menu():
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn.add(
        KeyboardButton("🔙назад"),
        KeyboardButton("🕵️‍♂️ Что ищут другие"),
        KeyboardButton("⚙️ Фильтр"),
        
 
    )
    return btn


async def bak_menu():
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn.add(
        KeyboardButton("🔙назад"),

        
 
    )
    return btn


tart_menu = ReplyKeyboardMarkup([
    [
    KeyboardButton("🔙назад")
    ],
    [
    KeyboardButton("недавно дабавленные"),
    KeyboardButton("топ рейтинга") 
    ],
    [
    KeyboardButton("Случайный материал"),
    KeyboardButton("по жанру"),
    ],
    [
    KeyboardButton("по году"),
    KeyboardButton("вы смотрели"),
    ],
    [
    KeyboardButton("сейчас смотрят"),  
    ]
])