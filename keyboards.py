
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton

inline1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="1",callback_data="n1"),
        InlineKeyboardButton(text="1",callback_data="n1"),
        InlineKeyboardButton(text="1",callback_data="n1"),
        InlineKeyboardButton(text="1",callback_data="n1"),
        InlineKeyboardButton(text="1",callback_data="n1"),
    ],
    [
        InlineKeyboardButton("[BCE]", callback_data="n6"),
        InlineKeyboardButton("ФИЛЬМЫ", callback_data="n7"),
        InlineKeyboardButton("СЕРИАЛЫ", callback_data="n8")
    ],
    [
        InlineKeyboardButton("СТРАНИЦА:1 ", callback_data="btn9"),
        InlineKeyboardButton("ВПЕРЁД⏭️", callback_data="btn10")
    ]
])


informatsiya = InlineKeyboardMarkup(
    inline_keyboard=[
    [
InlineKeyboardButton("купить подписку",callback_data="n1"),
    ],
    [
   InlineKeyboardButton("что делает  PREMIUM",callback_data="n2"), 
    ],
    [
 InlineKeyboardButton("ответи на вопросы",callback_data="n3") 
    ]

])

