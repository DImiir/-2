from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def first_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.<br>
    Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>
    И начнем с Марса!<br>
    Присоединяйся!'''


@app.route('/image_mars')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.tiff')}">
                    <h3>Вот она какая, красная планета.</h3>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.tiff')}">
                    <h3 class="alert alert-secondary" role="alert">Человечество вырастает из детства.</h3>
                    <h3 class="alert alert-success" role="alert">Человечеству мала одна планета.</h3>
                    <h3 class="alert alert-light" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</h3>
                    <h3 class="alert alert-warning" role="alert">И начнем с Марса!</h3>
                    <h3 class="alert alert-danger" role="alert">Присоединяйся!</h3>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
