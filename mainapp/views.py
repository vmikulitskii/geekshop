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
    content = {"title":title}
    return render(request, "mainapp/products.html",content)


def contact(request):
    title = 'о нас'
    visit_date = datetime.now()
    content = {"title":title,"visit_date":visit_date}
    return render(request, "mainapp/contact.html",content)