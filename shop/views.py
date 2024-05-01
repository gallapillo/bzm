from django.core.paginator import Paginator
from django.shortcuts import render

from shop.models import *


def index(request):
    page_obj = products = Product.objects.all()

    product_name = request.GET.get("search")

    if product_name != '' and product_name is not None:
        page_obj = products.filter(name__icontains=product_name)

    paginator = Paginator(page_obj, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }
    return render(request, 'shop/index.html', context=context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    discount_price = product.price - (product.price * (product.discount * 0.01))
    context = {
        "product": product,
        "discount_price": discount_price
    }
    return render(request, "shop/product_detail.html", context=context)
