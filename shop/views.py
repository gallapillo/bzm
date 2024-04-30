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
    discount_price = product.price - (product.price * (product.discount * 0.01))
    print("TEST IS " + discount_price.__str__())
    context = {
        "product": product,
        "discount_price": discount_price
    }
    return render(request, "shop/product_detail.html", context=context)
