from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Добро пожаловать в ReVitra Studio!\n\n"
        "Студия восстановления автомобильных стекол.\n\n"
        "Выберите действие 👇",
        reply_markup=main_menu
    )