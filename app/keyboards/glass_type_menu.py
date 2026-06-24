from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

glass_type_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лобовое")],
        [KeyboardButton(text="Боковые")],
        [KeyboardButton(text="Заднее")],
        [KeyboardButton(text="Вкруг")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)