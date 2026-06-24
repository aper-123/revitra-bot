import asyncio
import logging

from app.database import create_tables
from app.handlers.booking import router as booking_router
from app.handlers.contacts import router as contacts_router
from app.handlers.my_bookings import router as bookings_router
from app.handlers.start import router as start_router
from app.loader import bot, dp


async def main():
    logging.basicConfig(level=logging.INFO)
    create_tables()

    dp.include_router(start_router)
    dp.include_router(booking_router)
    dp.include_router(contacts_router)
    dp.include_router(bookings_router)

    print("====================================")
    print(" ReVitra Studio Bot started")
    print(" SQLite database connected")
    print("====================================")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
