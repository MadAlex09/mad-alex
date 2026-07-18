from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    print("ТЕКУЩАЯ ПАПКА:", os.getcwd())
    print("ФАЙЛЫ В ПАПКЕ:", os.listdir("."))
    print("TEMPLATES EXISTS:", os.path.exists("templates"))
    print("INDEX EXISTS:", os.path.exists("templates/index.html"))

    if request.method == "POST":

        name = request.form.get("name")
        contact = request.form.get("contact")
        message = request.form.get("message")

        print("Имя:", name)
        print("Контакт:", contact)
        print("Сообщение:", message)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)