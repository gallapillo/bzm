from django.shortcuts import render 
from shop.models import *

def index(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'shop/index.html', context=context)