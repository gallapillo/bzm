from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def orders_list(request):
    return render(request, "order/checkout.html")


@login_required
def checkout(request):
    return render(request, "order/order.html")
