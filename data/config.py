BOT_TOKEN = '5540685630:AAGcpKWbxUi0lpV4F-IPajrol722j0dLxtA'
from utils.db_api.sqlite import db

admins = db.select_all_adminss()
channels = db.select_all_channel()
id_list = [id[0] for id in channels]
CHANNELS = list(map(lambda x: x[0], channels))

ids = [id[0] for id in admins]
ADMINS = list(map(lambda x: x[0], admins))
texts = db.select_all_from_texts()

Button_text = [texts[0][1]]
Text_caption = [texts[0][0]]

btns = {
    "accept": "Tekshirish",
    "back": "Ortga qaytish",
    "new_test": "📚TEST VARIANTIGA BUYURTMA",
    "in_uzbek": "🇸🇱 O'zbekcha",
    "in_russian": "🇷🇺 Pусский",
    "dtm_news": "🛑 DTM Yangiliklari 🛑",
    "result": "🔠 Natijalarni bilish",
    "video_instruction": "🎥 Video qo'llanma",
    "blokli": "🏷 Testlar to'plamlari"
}

texts = {
    "text_to_start": f"<b>Assalomu alaykum! Botimizdan foydalanish uchun quyidagi kanallarga obuna bo'lishingiz kerak</b>",
    "main_menu": "Iltimos quyidagi menulardan birini tanlang!",
    "notaccepted": "❌<b> Quyidagi kanallarga a'zo bo'lmadingiz</b>, iltimos botdan foydalanish uchun kanalga a'zo bo'ling!",
    "accepted": "<b>Tabriklaymiz ✅,</b> Siz muvaffaqiyatli roʻyxatdan oʻtdingiz!",
    "select_test_language": "📖 Test varianti qaysi tilda bo'lishini ko'rsating: 👇",
    "menu": "<b>Siz bosh menudasiz, Quyidagi ko'rsatilgan menyudan o'zingizga kerakli bo'limni tanlang 👇</b>",
    "select_subject": "📗 Kerakli fanni tanlang: 👇",
    "ru_select_subject": "📗 Выберите нужную науку: 👇",
    "dtm_news": "Xabarni shu link orqali o'qishingiz mumkin \n\n https://t.me/davlat_test_markazi_online_test/132",
    "instruction": "<b>Quyidagi formatda test varianti javoblarini jo‘nating:\n\ntest raqami/abcdd</b>\nMasalan: 1011/abcde....",
    "caption_instruction": "<b>Botdan qanday foydalanishni bilmasangiz ushbu videoni ko'ring</b>"
}