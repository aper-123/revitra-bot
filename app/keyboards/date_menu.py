from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


date_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Сегодня")],
        [KeyboardButton(text="📅 Завтра")],
        [KeyboardButton(text="📅 Послезавтра")],
        [KeyboardButton(text="📅 Другая дата")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)