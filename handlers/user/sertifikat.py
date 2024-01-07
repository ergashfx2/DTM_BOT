from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.keyboard import mainM, back
from loader import dp


@dp.message_handler(text="🥇 Sertifikat olish")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer(f"*Ismingizni kiriting :*", reply_markup=back,parse_mode="markdown")
    await state.set_state("sertifikat")


@dp.message_handler(state="sertifikat")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer_photo(f"https://botlarga.uz/online.php?text={msg.text}",caption=f"{msg.text} *ismiga sertifikat tayyor\n\nBotimizni do'stlaringizga tavsiya qilishni unutmang*", reply_markup=back,parse_mode="markdown")
    await state.finish()
