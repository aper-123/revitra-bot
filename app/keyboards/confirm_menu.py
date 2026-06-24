from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


confirm_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Подтвердить запись")
        ],
        [
            KeyboardButton(text="✏️ Изменить"),
            KeyboardButton(text="❌ Отмена")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Подтвердите запись..."
)