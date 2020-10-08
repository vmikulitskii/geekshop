from django.shortcuts import render
from datetime import datetime
import json


def main(request):
    title = 'главная страница'
    with open('mainapp/products.json', 'r') as f:
        products = json.load(f)

    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = 'товары'
    with open('mainapp/links_menu.json', 'r') as f:
        links_menu = json.load(f)

    with open('mainapp/same_products.json', 'r') as f:
        same_products = json.load(f)

    content = {"title": title, 'links_menu': links_menu,
               "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = 'о нас'
    visit_date = datetime.now()

    with open('mainapp/locations.json', 'r') as f:
        locations = json.load(f)

    content = {"title": title, "visit_date": visit_date,
               "locations": locations}
    return render(request, "mainapp/contact.html", content)
