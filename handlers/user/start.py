from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.user.admin import create_user
from keyboards.default.keyboard import mainM
from keyboards.default.Sinflar import Sinflar
from loader import dp

from keyboards.default.blok import blok


@dp.message_handler(text="Ortga qaytish", state=["mother", "matem"])
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer(f"Kerakli fanni tanlang", reply_markup=blok)
    await state.finish()


@dp.message_handler(text="Ruxsatnomani yulab olish")
async def welcome(msg: types.Message, state: FSMContext):
    await msg.answer(
        "👨🏻‍💻 Abituriyentlar test sinovlarida ishtirok etish uchun “Abituriyent ruxsatnomasi”ni my.dtm.uz saytiga shaxsiy identifikatsiya raqami hamda pasport seriyasi va raqamini kiritgan holda olishlari mumkin.\n\n📥 Shuningdek, ruxsatnomani Davlat test markazining quyidagi maxsus telegram botlari orqali ham yuklab olish imkoniyati mavjud:\n\n👉 @e_dtm_mandatbot\n👉 @e_dtm_mandat1bot\n👉 @e_dtm_mandat2bot\n👉 @e_dtm_mandat3bot\n👉 @e_dtm_mandat4bot\n\n📆 Test sinovlari 8-avgustdan boshlanishini inobatga olgan holda abituriyentlardan ruxsatnomalarni 7-avgustga qadar yuklab olishlarini so‘raymiz.\n\n📌 Eslatib o‘tamiz, abituriyentlar test sinovlariga pasport (ID-karta) va abituriyent ruxsatnomasi bilan kelishlari lozim.")


@dp.message_handler(text=["/start", "Ortga qaytish"])
async def welcome(msg: types.Message, state: FSMContext):
    name = msg.from_user.full_name
    await msg.answer(f"Salom {name}", reply_markup=mainM)
    await state.finish()


@dp.message_handler(text="Matematika (5-11)", state="blokli")
async def welcome(msg: types.Message, state: FSMContext):
    name = msg.from_user.full_name
    await msg.answer(f"*Kerakli sinfni tanlang*", reply_markup=Sinflar, parse_mode="markdown")
    await state.set_state("matem")


@dp.message_handler(text="Ona tili (5-11)", state="blokli")
async def welcome(msg: types.Message, state: FSMContext):
    name = msg.from_user.full_name
    await msg.answer(f"*Kerakli sinfni tanlang*", reply_markup=Sinflar, parse_mode="markdown")
    await state.set_state("mother")


@dp.message_handler(state="matem")
async def welcome(msg: types.Message, state: FSMContext):
    sinf = msg.text[:2]
    son = int(sinf)
    raqami = 222 + son
    await msg.answer_document(f"https://t.me/testiszlar/{raqami}", caption=f"{sinf} *Sinf matematika testlar to'plami*",
                              reply_markup=Sinflar, parse_mode="markdown")


@dp.message_handler(state="mother")
async def welcome(msg: types.Message, state: FSMContext):
    sinf = msg.text[:2]
    son = int(sinf)
    raqami = 215 + son
    await msg.answer_document(f"https://t.me/testiszlar/{raqami}",
                              caption=f"{sinf} *Sinf Ona tili fanidan testlar to'plami*", reply_markup=Sinflar,
                              parse_mode="markdown")
