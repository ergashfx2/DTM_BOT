from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.config import btns
lesson = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="🇺🇸 Ingliz tili"),
    ],
    [
        KeyboardButton(text="🇺🇿 Ona tili")
    ],
    [
        KeyboardButton(text="🇺🇿 Matematika"),
    ],
    [
        KeyboardButton(text=btns["back"])
    ]

],
    resize_keyboard=True,
)