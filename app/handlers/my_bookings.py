from aiogram import F, Router
from aiogram.types import Message

router = Router()


@router.message(F.text == "📅 Мои записи")
async def bookings(message: Message):
    await message.answer(
        "У вас пока нет активных записей."
    )