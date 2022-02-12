from flask import Flask, render_template, url_for

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]

app = Flask(__name__)


@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="О сайте", menu=menu)

@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"

if __name__ == "__main__":
    app.run(debug=True)
