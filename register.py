import sqlite3


def user_exists(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT telegram_id FROM users WHERE telegram_id=?",
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user is not None


def add_user(user_id, name, phone):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users VALUES (?, ?, ?)",
        (user_id, name, phone)
    )

    conn.commit()
    conn.close()


def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE telegram_id=?",
        (user_id,)
    )

    conn.commit()
    conn.close()