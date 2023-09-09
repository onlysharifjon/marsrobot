from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Uzb", callback_data="Uzbek"),
            InlineKeyboardButton(text="Eng", callback_data="English"),
            InlineKeyboardButton(text="Rus", callback_data="Russian")
        ],
    ],
)
who = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ota Onaman', callback_data='ota'),
            InlineKeyboardButton(text='Studentman', callback_data='stud'),
            InlineKeyboardButton(text='Mehmonman', callback_data='meh'),
        ]
    ]
)
