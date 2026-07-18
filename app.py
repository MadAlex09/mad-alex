from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form.get("name")
        contact = request.form.get("contact")
        message = request.form.get("message")

        print()
        print("========== НОВАЯ ЗАЯВКА ==========")
        print("Имя:", name)
        print("Контакт:", contact)
        print("Сообщение:", message)
        print("===================================")
        print()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)