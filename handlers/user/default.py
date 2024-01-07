from aiogram import types

from data.config import texts
from handlers.user.admin import create_user
from loader import dp


@dp.message_handler()
async def test(msg: types.Message):
    await msg.answer(texts["main_menu"])
