from django.core.paginator import Paginator
from django.db.models import Q
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
    category = product.category
    related_products = Product.objects.filter(~Q(id=id), category=category)
    context = {
        "product": product,
        "discount_price": discount_price,
        "related_products": related_products
    }
    return render(request, "shop/product_detail.html", context=context)


def brands(request):
    brands_items = Brand.objects.all()
    context = {
        "brands": brands_items
    }
    return render(request, "shop/brands.html", context=context)


def brand_detail(request, id):
    brand = Brand.objects.get(id=id)
    product_brand = Product.objects.filter(brand__name=brand.name)
    categories_lst = list(product_brand.values_list("category", flat=True))
    categories_set = set(categories_lst)

    categories = Category.objects.none()
    for cat in categories_set:
        categories |= Category.objects.filter(id=cat)

    context = {
        "categories": categories,
        "brand": brand
    }
    return render(request, "shop/brand.html", context=context)


def categories(request):
    categories_items = Category.objects.all()
    context = {
        "categories": categories_items
    }
    return render(request, "shop/category/categories.html", context=context)


def category_detail(request, id, brand_id):
    category = Category.objects.get(id=id)
    page_obj = products = Product.objects.filter(category=category)

    product_name = request.GET.get("search")

    if brand_id != '' and brand_id is not None:
        page_obj = products.filter(brand__in=str(brand_id))

    if product_name != '' and product_name is not None:
        page_obj = products.filter(name__icontains=product_name, brand__in=str(brand_id))

    paginator = Paginator(page_obj, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "category": category,
        "page_obj": page_obj
    }
    return render(request, "shop/category/category.html", context=context)
