from aiogram import F, Router
from aiogram.types import Message

from app.config import ADMIN_ID
from app.data.services import SERVICES
from app.keyboards.main_menu import main_menu
from app.keyboards.services_menu import create_services_menu
from app.keyboards.options_menu import create_options_keyboard
from app.keyboards.date_menu import date_menu
from app.keyboards.contact_menu import contact_menu
from app.keyboards.confirm_menu import confirm_menu
from app.storage.booking_storage import bookings
from app.loader import bot

router = Router()


def create_booking():
    return {
        "screen": "",
        "service": "",
        "option": "",
        "date": "",
        "name": "",
        "phone": "",
        "photo": None
    }


@router.message(F.text == "🚗 Записаться")
async def booking(message: Message):

    bookings[message.from_user.id] = create_booking()
    bookings[message.from_user.id]["screen"] = "services"

    await message.answer(
        "Выберите услугу:",
        reply_markup=create_services_menu()
    )


@router.message(lambda message: message.text in SERVICES)
async def choose_service(message: Message):

    user = bookings[message.from_user.id]

    user["service"] = message.text
    user["screen"] = "options"

    await message.answer(
        "Выберите вариант:",
        reply_markup=create_options_keyboard(
            SERVICES[message.text]["options"]
        )
    )


@router.message(
    F.text.in_([
        "Лобовое",
        "Боковые",
        "Заднее",
        "Вкруг",
        "Передние",
        "Задние",
        "Все",
        "Передние боковые",
        "Все стекла",
        "1 скол",
        "2 скола",
        "3 и более"
    ])
)
async def choose_option(message: Message):

    user = bookings[message.from_user.id]

    user["option"] = message.text
    user["screen"] = "date"

    await message.answer(
        "Выберите дату:",
        reply_markup=date_menu
    )


@router.message(
    F.text.in_([
        "📅 Сегодня",
        "📅 Завтра",
        "📅 Послезавтра"
    ])
)
async def choose_date(message: Message):

    user = bookings[message.from_user.id]

    user["date"] = message.text
    user["screen"] = "name"

    await message.answer("Введите Ваше имя:")


@router.message(
    lambda message: message.from_user.id in bookings
    and bookings[message.from_user.id]["screen"] == "name"
)
async def enter_name(message: Message):

    user = bookings[message.from_user.id]

    user["name"] = message.text
    user["screen"] = "phone"

    await message.answer(
        "Нажмите кнопку ниже и поделитесь номером телефона.",
        reply_markup=contact_menu
    )


@router.message(F.contact)
async def enter_phone(message: Message):

    if message.from_user.id not in bookings:
        return

    user = bookings[message.from_user.id]

    if user["screen"] != "phone":
        return

    user["phone"] = message.contact.phone_number
    user["screen"] = "confirm"

    text = (
        "📋 Проверьте заявку\n\n"
        f"🏢 ReVitra Studio\n\n"
        f"🚗 Услуга:\n{user['service']}\n\n"
        f"🔧 Вариант:\n{user['option']}\n\n"
        f"📅 Дата:\n{user['date']}\n\n"
        f"👤 Имя:\n{user['name']}\n\n"
        f"📱 Телефон:\n{user['phone']}"
    )

    await message.answer(
        text,
        reply_markup=confirm_menu
    )


@router.message(F.text == "✅ Подтвердить запись")
async def confirm_booking(message: Message):

    if message.from_user.id not in bookings:
        return

    user = bookings[message.from_user.id]

    text = (
        "🔔 Новая запись\n\n"
        f"👤 {user['name']}\n"
        f"📱 {user['phone']}\n\n"
        f"🚗 {user['service']}\n"
        f"🔧 {user['option']}\n"
        f"📅 {user['date']}\n\n"
        f"Telegram: @{message.from_user.username or 'не указан'}"
    )

    await bot.send_message(
        ADMIN_ID,
        text
    )

    bookings.pop(message.from_user.id)

    await message.answer(
        "✅ Спасибо!\n\n"
        "Ваша заявка успешно отправлена.\n"
        "Мы свяжемся с вами в ближайшее время.",
        reply_markup=main_menu
    )


@router.message(F.text == "❌ Отмена")
async def cancel_booking(message: Message):

    bookings.pop(message.from_user.id, None)

    await message.answer(
        "Запись отменена.",
        reply_markup=main_menu
    )


@router.message(F.text == "⬅️ Назад")
async def back(message: Message):

    await message.answer(
        "Главное меню",
        reply_markup=main_menu
    )