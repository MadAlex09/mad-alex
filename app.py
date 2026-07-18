from flask import Flask, render_template, request
import os
import requests
import asyncio

from main import bot, dp
from aiogram.types import Update


app = Flask(__name__)


BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = "8103221216"

WEBHOOK_PATH = "/telegram-webhook"
WEBHOOK_URL = os.getenv("WEBHOOK_URL")



# =========================
# Установка webhook
# =========================

if WEBHOOK_URL:

    asyncio.run(
        bot.set_webhook(
            url=WEBHOOK_URL + WEBHOOK_PATH
        )
    )

    print("✅ Telegram webhook установлен")


# =========================
# Telegram webhook
# =========================

@app.route(WEBHOOK_PATH, methods=["POST"])
def telegram_webhook():

    print("📩 ПОЛУЧЕН TELEGRAM UPDATE")

    data = request.get_json()

    update = Update.model_validate(data)

    print("📦 UPDATE СОЗДАН")

    async def process_update():

        try:

            await dp.feed_update(
                bot,
                update
            )

            print("✅ AIROGRAM ОБРАБОТАЛ UPDATE")

        except Exception as error:

            print("❌ ОШИБКА AIROGRAM:")
            print(repr(error))

    asyncio.run(process_update())

    return "OK"


# =========================
# Сайт
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form.get("name")
        contact = request.form.get("contact")
        message = request.form.get("message")

        text = f"""
🔔 НОВАЯ ЗАЯВКА С САЙТА

👤 Имя: {name}

📱 Контакт: {contact}

💬 Сообщение:
{message}
"""

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(
            url,
            data={
                "chat_id": ADMIN_ID,
                "text": text
            }
        )

        print("✅ Заявка отправлена в Telegram")

    return render_template("index.html")


# =========================
# Локальный запуск
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )