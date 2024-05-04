from django.urls import path

from order import views

urlpatterns = [
    path('', views.orders_list, name="orders"),
    path('checkout', views.checkout, name="orders_checkout")
]
