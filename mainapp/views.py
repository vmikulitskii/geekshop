from django.shortcuts import render

def main(request):
    return render(request, "mainapp/index.html")

def products(request):
    return render(request, "mainapp/products.html")

def contact(request):
    return render(request, "mainapp/contact.html")

def productsdetail(request):
    return render(request, "mainapp/productsdetail.html")


# Create your views here.
