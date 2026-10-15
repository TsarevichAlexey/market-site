from django.contrib import admin

from .models import Category, Product

#Все это данные для регистрации вещей в админ-панели сайта 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug']#Параметры, которые будут видны в админке
    prepopulated_fields = {'slug':('name', )} #автоматическое заполнение slug для нужных товаров 

#Регистрация продукта
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created','updated']
    list_filter = ['available', 'created', 'updated', 'category']

    #Позволяет выбрать параметры, которые можно изменить в админке
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug':('name',)}
