from flask import Flask, render_template, request
import os
import requests
import asyncio
import threading

from main import bot, dp
from aiogram.types import Update


app = Flask(__name__)


BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = "8103221216"

WEBHOOK_PATH = "/telegram-webhook"
WEBHOOK_URL = os.getenv("WEBHOOK_URL")


# =========================
# Отдельный event loop для бота
# =========================

bot_loop = asyncio.new_event_loop()


def start_bot_loop():
    asyncio.set_event_loop(bot_loop)
    bot_loop.run_forever()


threading.Thread(
    target=start_bot_loop,
    daemon=True
).start()


# =========================
# Установка webhook
# =========================

if WEBHOOK_URL:

    future = asyncio.run_coroutine_threadsafe(
        bot.set_webhook(
            url=WEBHOOK_URL + WEBHOOK_PATH
        ),
        bot_loop
    )

    future.result()

    print("✅ Telegram webhook установлен")


# =========================
# Telegram webhook
# =========================

@app.route(WEBHOOK_PATH, methods=["POST"])
def telegram_webhook():

    data = request.get_json()

    update = Update.model_validate(data)

    asyncio.run_coroutine_threadsafe(
        dp.feed_update(
            bot,
            update
        ),
        bot_loop
    )

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