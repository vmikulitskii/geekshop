from basketapp.views import basket
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Contact, Product, ProductCategory
from basketapp.models import Basket


def main(request):
    title = 'главная страница'
    # with open('mainapp/products.json', 'r') as f:
    #     products = json.load(f)

    products = Product.objects.all()[:4]

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
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk).order_by('price')
        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products,
            "media_url": settings.MEDIA_URL,
            "basket": basket,

        }
        return render(request, "mainapp/products_list.html", content)

    same_products = Product.objects.all()

    content = {"title": title, 'links_menu': links_menu,
               "same_products": same_products, "media_url": settings.MEDIA_URL, "basket": basket, }

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
