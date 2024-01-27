# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.


# Внутри каждого представления должна быть переменная html —
# многострочный текст с HTML-вёрсткой и данными
# о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.

from django.http import HttpResponse
import logging
from datetime import timezone, datetime
from django.shortcuts import render
from .models import User, Order
from .forms import ItemPictureForm

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


def order_list(request, user_id):
    user = User.objects.get(id=user_id)
    orders = Order.objects.filter(user=user).order_by('-order_date')

    def filter_orders_last_n_days(n):
        end_date = timezone.now()
        start_date = end_date - datetime.timedelta(days=n)
        return orders.filter(order_date__range=[start_date, end_date])

    orders_last_7_days = filter_orders_last_n_days(7)
    orders_last_30_days = filter_orders_last_n_days(30)
    orders_last_365_days = filter_orders_last_n_days(365)

    context = {
        'user': user,
        'orders_last_7_days': orders_last_7_days,
        'orders_last_30_days': orders_last_30_days,
        'orders_last_365_days': orders_last_365_days,
    }

    return render(request, 'order_list.html', context)


def item_picture_form(request):
    if request.method == 'POST':
        form = ItemPictureForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            picture = form.cleaned_data['picture']
            logger.info(f'Добавлен товар {title}, цена: {price}')
    else:
        form = ItemPictureForm()

    return render(request, 'homework_app/item_picture_form.html', {'form': form})