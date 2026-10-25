"""Это urls приложения"""
#Указывает путь для url
from django.urls import path

from . import views

#Имя приложения соответствует названию папки
app_name = 'main'

urlpatterns = [
    #главный путь при открытии
    #подгружает данные из ./views.py
    # Созданные urls нужно зарегистрировать в главном urls
    path('', views.product_list, name='product_list'),

    #Путь на фильтрацию по категориям
    #Валидация url
    path('<slug:category_slug>/',views.product_list, 
         name='product_list_by_category'),

    #Путь для детальной информации о товаре
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),
]