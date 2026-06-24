from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


contact_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📱 Поделиться номером",
                request_contact=True
            )
        ],
        [
            KeyboardButton(text="⬅️ Назад")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Поделитесь номером телефона..."
)