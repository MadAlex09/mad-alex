import sqlite3


DB_NAME = "database.db"


# ======================
# Создание базы
# ======================

def create_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        name TEXT,

        place TEXT,

        hours INTEGER,

        date TEXT,

        start_time TEXT

    )
    """)

    conn.commit()
    conn.close()



# ======================
# Добавить бронь
# ======================

def add_booking(
        user_id,
        name,
        place,
        hours,
        date,
        start_time
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bookings
    (
        user_id,
        name,
        place,
        hours,
        date,
        start_time
    )

    VALUES (?, ?, ?, ?, ?, ?)

    """,
    (
        user_id,
        name,
        place,
        hours,
        date,
        start_time
    ))

    conn.commit()
    conn.close()



# ======================
# Проверка занятости
# ======================

def check_booking(
        place,
        date,
        start_time
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute("""
    SELECT id 
    FROM bookings

    WHERE place = ?
    AND date = ?
    AND start_time = ?

    """,
    (
        place,
        date,
        start_time
    ))


    result = cursor.fetchone()


    conn.close()


    if result:
        return True

    return False