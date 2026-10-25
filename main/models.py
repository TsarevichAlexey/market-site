from django.db import models

from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index= True)#db_index?! Используется к параметру, к которому часто применяется сортировка
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:#параметры с которыми будет работать бд и админка
        ordering = ('name',) #как будут располагаться наши товары, т.е. сортировка по имени
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):#Определяет как будет отображаться элемент, здесь в админке
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:product_list_by_category", kwargs={"pk": self.pk})
    
    

class Product (models.Model):
    #Подгружаем категорию, другого класса (позволяет вставить уже созданные объекты)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    
    slug = models.SlugField(max_length=100, unique=True)#Уникальные url
    
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank = True)#Заполнять необязательно
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
