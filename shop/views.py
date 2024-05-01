from django.shortcuts import render
from django.views.generic import ListView

from shop.models import *


# def index(request):
#     products = Product.objects.all()
#     context = {
#         "products": products
#     }
#     return render(request, 'shop/index.html', context=context)

class ProductListView(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"
    paginate_by = 12


def product_detail(request, id):
    product = Product.objects.get(id=id)
    discount_price = product.price - (product.price * (product.discount * 0.01))
    print("TEST IS " + discount_price.__str__())
    context = {
        "product": product,
        "discount_price": discount_price
    }
    return render(request, "shop/product_detail.html", context=context)
