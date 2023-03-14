from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def return_sample_page(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_mars.css')}" />
                    <title>Результаты!</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h3>Претендент на участие в миссии {nickname}:</h3>
                    <br><label class="green">Поздравляем! Ваш рейтинг после {level} этапа отбора</label>
                    <br><label>оставляет {rating}!</label>
                    <br><label class="yellow">Желаем удачи!</label>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8075, host='127.0.0.1')