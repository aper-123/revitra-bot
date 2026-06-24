import sqlite3
from pathlib import Path

# Папка проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Файл базы данных
DB_PATH = BASE_DIR / "revitra.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL,
            username TEXT,
            service TEXT NOT NULL,
            option TEXT NOT NULL,
            booking_date TEXT NOT NULL,
            customer_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            status TEXT DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_booking(
    telegram_id: int,
    username: str,
    service: str,
    option: str,
    booking_date: str,
    customer_name: str,
    phone: str,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO bookings (
            telegram_id,
            username,
            service,
            option,
            booking_date,
            customer_name,
            phone
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            telegram_id,
            username,
            service,
            option,
            booking_date,
            customer_name,
            phone,
        ),
    )

    conn.commit()
    conn.close()


def is_date_busy(booking_date: str) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM bookings
        WHERE booking_date = ?
        AND status = 'active'
        """,
        (booking_date,),
    )

    result = cursor.fetchone()[0]

    conn.close()

    return result > 0


def get_all_bookings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM bookings
        ORDER BY booking_date
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_booking(booking_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM bookings
        WHERE id = ?
        """,
        (booking_id,),
    )

    conn.commit()
    conn.close()