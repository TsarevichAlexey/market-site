
from django.contrib import admin
from django.urls import path, include

#Выводит определенные страницы исходя из пути
urlpatterns = [
    path('admin/', admin.site.urls),
    #namespace пр-во имен, то есть различные url маршруты для различения
    #между приложениями.
    #Допустим есть одинаковый url detail, но в каждом приложении он свой 
    path('',include("main.urls", namespace='main')),
]
