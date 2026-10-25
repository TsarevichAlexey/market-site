from django.shortcuts import render, get_object_or_404

from .models import Category, Product


"""Можно использовать классовое представление (для больших представлений)"""
def product_list(request, category_slug=None):#параметры запроса для фильтрации
    #Выводит все категории из бд в шаблоне
    categories = Category.objects.all()
    #Параметр для фильтрации(берется из модели model.py)
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        #через get делаем запрос и возвращаем или объект или ошибку
        # В качестве параметра указываем slug, переданный пользователем
        category = get_object_or_404(Category, category_slug=category_slug)

        products = products.filter(category=category)

    #Возвращает вид страницы (через шаблон во второй странице)
    return render(request, 'main/product/list.html',
                  {'category': category,
                  'categories':categories,
                  'products':products})
#Страница о товаре
def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id, slug=slug, available=True)

    """Выводит похожие товары, которые определяет по одной категории
    фильтрует и исключает текущий продукт.
    Здесь огрничено 4 товарами"""
    related_products = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:4]

    return render (request, 'main/product/detail.html', {'product':product, 'related_products':related_products})