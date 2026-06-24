from aiogram import F, Router
from aiogram.types import Message

router = Router()


@router.message(F.text == "📞 Контакты")
async def contacts(message: Message):
    await message.answer(
        "📍 ReVitra Studio\n\n"
        "Работаем 24/7"
    )