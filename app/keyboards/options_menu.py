from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_options_keyboard(options: list[str]) -> ReplyKeyboardMarkup:
    keyboard = []

    for option in options:
        keyboard.append([KeyboardButton(text=option)])

    keyboard.append([KeyboardButton(text="⬅️ Назад")])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите вариант..."
    )