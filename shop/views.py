from django.shortcuts import render 
from shop.models import *

def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'shop/index.html', context=context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product
    }
    return render(request, "shop/product_detail.html", context=context)