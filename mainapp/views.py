from django.conf import settings
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
import json
from .models import Product, ProductCategory


def main(request):
    title = 'главная страница'
    # with open('mainapp/products.json', 'r') as f:
    #     products = json.load(f)

    products = Product.objects.all()

    content = {"title": title, "products": products,
               'media_url': settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = 'товары'
    # with open('mainapp/links_menu.json', 'r') as f:
    #     links_menu = json.load(f)

    # with open('mainapp/same_products.json', 'r') as f:
    #     same_products = json.load(f)
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()

    content = {"title": title, 'links_menu': links_menu,
               "same_products": same_products, "media_url": settings.MEDIA_URL, }

    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date,
               "locations": locations}
    return render(request, "mainapp/contact.html", content)
