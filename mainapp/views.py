from django.shortcuts import render
from datetime import datetime


def main(request):
    title = 'главная страница'
    products = [
        {
            "name": "Теплый ламповый стул",
            "desc": "Расположитесь комфортно.",
            "image_src": "product-1.jpg",
            "image_href": "/product/1/",
            "alt": "продукт 1",
        },
         {
            "name": "Кресло для любителей картошки фри",
            "desc": "Вы точно в нем поместитесь.",
            "image_src": "product-3-sm.jpg",
            "image_href": "/product/3/",
            "alt": "продукт 3",
        },
        {
            "name": "Стул для близнецов",
            "desc": "Уже не стул, еще не кресло.",
            "image_src": "product-2.jpg",
            "image_href": "/product/2/",
            "alt": "продукт 2",
        }
    ]
    content = {"title":title,"products":products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = 'товары'
   

    links_menu = [
        {"href": "products_all", "name": "все"},
        {"href": "products_home", "name": "дом"},
        {"href": "products_office", "name": "офис"},
        {"href": "products_modern", "name": "модерн"},
        {"href": "products_classic", "name": "классика"},
    ]

    same_products = [
        {
            "name": "Отличный стул",
            "desc": "Не оторваться.",
            "image_src": "product-11.jpg", "alt": "продукт 11"
        },
            
        {
            "name": "Стул повышенного качества",
            "desc": "Комфортно.",
            "image_src": "product-21.jpg",
            "alt": "продукт 21"
        },

        {
            "name": "Стул премиального качества",
            "desc": "Просто попробуйте.",
            "image_src": "product-31.jpg",
            "alt": "продукт 31",
        },
    ]
    content = {"title":title, 'links_menu':links_menu, "same_products":same_products}
    return render(request, "mainapp/products.html",content)


def contact(request):
    title = 'о нас'
    visit_date = datetime.now()

    locations = [
        {
            "city": "Москва",
            "phone": "+7-888-888-8888",
            "email": "info@geekshop.ru",
            "address": "Метро Чертаново, спросить любого"},
        {
            "city": "Екатеринбург",
            "phone": "+7-777-777-7777",
            "email": "info_yekaterinburg@geekshop.ru",
            "address": "Рядом с плотинкой",
        },
        {
            "city": "Нижний Тагил",
            "phone": "+7-999-999-9999",
            "email": "lower_tagil@geekshop.ru",
            "address": "Близко к заводу",
        },
    ]
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html",content)
    