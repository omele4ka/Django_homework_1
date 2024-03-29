from django.urls import path
from . import views
from .views import order_list, item_picture_form


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('order_list/<int:user_id>/', views.order_list, name='order_list'),
    path('item_picture_form/', item_picture_form, name='item_picture_form'),
]