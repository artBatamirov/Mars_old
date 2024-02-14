from flask import Flask, url_for, request

app = Flask(__name__)
link = ''

@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promote():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '<br>'.join(lst)


@app.route('/image_mars')
def show_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename='img/mars.png')}>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promote_image():
    lst = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']

    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src={url_for('static', filename='img/mars.png')}>
                        <div class="alert alert-secondary" role="alert">
                          <h5>{lst[0]}</h5>
                        </div>
                        <div class="alert alert-success" role="alert">
                          <h5>{lst[1]}</h5>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          <h5>{lst[2]}</h5>
                        </div>
                        <div class="alert alert-warning" role="alert">
                          <h5>{lst[3]}</h5>
                        </div>
                        <div class="alert alert-danger" role="alert">
                          <h5>{lst[4]}</h5>
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def show_result(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                            <title>Результаты</title>

                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h2>Претендента на участие в миссии {nickname}:</h2>
                            <div class="alert alert-success" role="alert">
                              <h5>Поздравляем! Ваш рейтинг после {level} этапа отбора</h5>
                            </div>
                            <div >
                              <h5>составляет {rating}!</h5>
                            </div>
                            <div class="alert alert-warning" role="alert">
                              <h5>Желаем удачи!</h5>
                            </div>
                          </body>
                        </html>'''
@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    global link
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1 align="center">Загрузка фотографии</h1>
                                <h2 align="center">для участия в миссии</h2
                                <div>
                                    <form class="login_form" method="post">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        link = request.form['file']
        return f'''<!doctype html>
                                    <html lang="en">
                                      <head>
                                        <meta charset="utf-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                        <link rel="stylesheet"
                                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                        crossorigin="anonymous">
                                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                        <title>Пример формы</title>
                                      </head>
                                      <body>
                                        <h1 align="center">Загрузка фотографии</h1>
                                        <h2 align="center">для участия в миссии</h2
                                        <div>
                                            <form class="login_form" method="post">
                                                <div class="form-group">
                                                    <label for="photo">Приложите фотографию</label>
                                                    <input type="file" class="form-control-file" id="photo" name="file">
                                                </div>
                                                
                                                <img src={url_for('static', filename='img/' + link)} width=60% align=bottom>
                                                <br>
                                                <button type="submit" class="btn btn-primary">Отправить</button>
                                            </form>
                                        </div>
                                      </body>
                                    </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
