# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.

# Внутри каждого представления должна быть переменная html —
# многострочный текст с HTML-вёрсткой и данными
# о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.

from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)

def index(request):
    logger.info('index was requested')
    html = """
        <html>
            <head>
                <title>Мой первый Django-сайт</title>
            </head>
            <body>
                <h1>Добро пожаловать на главную страницу!</h1>
                <p>Это мой первый Django-сайт.</p>
                <p>Здесь вы найдете информацию обо мне и о моем проекте.</p>
            </body>
        </html>
    """
    return HttpResponse(html)

def about(request):
    logger.info('about us was requested')
    html = """
        <html>
            <head>
                <title>Обо мне</title>
            </head>
            <body>
                <h1>Обо мне</h1>
                <p>Это страница с информацией о моем проекте.</p>
                <p>Я работаю над созданием удивительного веб-приложения с использованием Django.</p>
            </body>
        </html>
    """
    return HttpResponse(html)

