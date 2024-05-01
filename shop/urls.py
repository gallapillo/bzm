from shop import views
from django.urls import path

urlpatterns= [
    path('', views.ProductListView.as_view(), name="index"),
    path('product/<int:id>/', views.product_detail, name="product_detailW")
]