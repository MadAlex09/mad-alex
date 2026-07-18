from flask import Flask, render_template, request
import os
import requests


app = Flask(__name__)


BOT_TOKEN = os.getenv("8709000302:AAGklJSGXAZDDq5z_RTx14uHL2LQbjpB-Is")
ADMIN_ID = "8103221216"


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

        print("Заявка отправлена в Telegram")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)