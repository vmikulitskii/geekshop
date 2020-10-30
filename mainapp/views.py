import random
from django.contrib.auth import authenticate
from django.http import request
from basketapp.views import basket
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Contact, Product, ProductCategory
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def main(request):
    title = 'главная страница'
    # with open('mainapp/products.json', 'r') as f:
    #     products = json.load(f)

    products = Product.objects.all()[:4]

    content = {"title": title, "products": products,
               'media_url': settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    products = Product.objects.all()
    return random.choice(list(products))


def get_same_products(hot_product):
    same_products = Product.objects.filter(
        category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def product(request,pk):
    title = 'продукты'
    content = {
        "title":title,
        "links_menu": ProductCategory.objects.filter(is_active=True),
        "product":get_object_or_404(Product,pk=pk),
        "basket":get_basket(request.user),
        "media_url":settings.MEDIA_URL,

    }
    return render(request,"mainapp/product.html",content)

def products(request, pk=None, page=1):
    title = 'товары'
    # with open('mainapp/links_menu.json', 'r') as f:
    #     links_menu = json.load(f)

    # with open('mainapp/same_products.json', 'r') as f:
    #     same_products = json.load(f)
    links_menu = ProductCategory.objects.filter(is_active=True)
    basket = get_basket(user=request.user)

    if pk is not None:
        if pk == 0:
            category = {"pk": 0, "name": "все"}
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by("price")
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                "price"
            )

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products_paginator,
            "media_url": settings.MEDIA_URL,
            "basket": basket,
        }
        return render(request, "mainapp/products_list.html", content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {"title": title, 'links_menu': links_menu,
               "same_products": same_products, "media_url": settings.MEDIA_URL, "basket": basket, "hot_product": hot_product, }

    if pk:
        print(f"User select category: {pk}")
    category = {'name': 'все'}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date,
               "locations": locations}
    return render(request, "mainapp/contact.html", content)
