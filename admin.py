from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import os

ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
from aiogram import F
from admin_keyboard import admin_menu

import sqlite3


router = Router()


DB_NAME = "database.db"



# ======================
# Все брони
# ======================

@router.message(Command("bookings"))
async def all_bookings(message: Message):

    if message.from_user.id != ADMIN_ID:
        await message.answer(
            "❌ Нет доступа"
        )
        return


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT 
    name,
    place,
    hours,
    date,
    start_time

    FROM bookings

    ORDER BY id DESC
    """)


    bookings = cursor.fetchall()


    conn.close()


    if not bookings:

        await message.answer(
            "📋 Броней пока нет"
        )

        return



    text = "📋 Все брони:\n\n"


    for booking in bookings:

        name = booking[0]
        place = booking[1]
        hours = booking[2]
        date = booking[3]
        start = booking[4]


        text += (
            f"👤 {name}\n"
            f"🖥 {place}\n"
            f"⏳ {hours} час(а)\n"
            f"📅 {date}\n"
            f"⏰ {start}\n"
            f"────────────\n"
        )


    await message.answer(text)

@router.message(Command("admin"))
async def admin_panel(message: Message):

    if message.from_user.id != ADMIN_ID:
        await message.answer(
            "❌ Нет доступа"
        )
        return


    await message.answer(
        "👑 Админ-панель",
        reply_markup=admin_menu
    )

@router.message(F.text == "📋 Все брони")
async def button_bookings(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT 
    id,
    name,
    place,
    hours,
    date,
    start_time

    FROM bookings
    """)


    rows = cursor.fetchall()

    conn.close()


    if not rows:

        await message.answer(
            "📋 Броней нет"
        )

        return


    text = "📋 Брони:\n\n"


    for row in rows:

        text += (
            f"🆔 {row[0]}\n"
            f"👤 {row[1]}\n"
            f"🖥 {row[2]}\n"
            f"⏳ {row[3]} час\n"
            f"📅 {row[4]}\n"
            f"⏰ {row[5]}\n"
            f"────────────\n"
        )


    await message.answer(text)

@router.message(F.text == "❌ Удалить бронь")
async def delete_booking_start(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        "Введите ID брони, которую нужно удалить:\n\n"
        "Посмотреть ID можно через кнопку 📋 Все брони"
    )

@router.message(F.text.isdigit())
async def delete_booking(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    booking_id = int(message.text)


    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        "DELETE FROM bookings WHERE id = ?",
        (booking_id,)
    )


    conn.commit()


    deleted = cursor.rowcount


    conn.close()


    if deleted:

        await message.answer(
            f"✅ Бронь №{booking_id} удалена"
        )

    else:

        await message.answer(
            "❌ Такой брони нет"
        )