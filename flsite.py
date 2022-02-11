from flask import Flask, render_template

menu = ["Установка", "Первое приложение", "Обратная связь"]

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="О сайте", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
