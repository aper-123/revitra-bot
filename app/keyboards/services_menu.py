from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data.services import SERVICES


def create_services_menu():

    keyboard = []

    for service in SERVICES:
        keyboard.append(
            [KeyboardButton(text=service)]
        )

    keyboard.append(
        [KeyboardButton(text="⬅️ Назад")]
    )

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите услугу..."
    )