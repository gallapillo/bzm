from shop import views
from django.urls import path

urlpatterns= [
    path('', views.index, name="index"),
    path('product/<int:id>/', views.product_detail, name="product_detail"),
    path('brands/', views.brands, name="brands"),
    path('brand/<int:id>', views.brand_detail, name="brand_detail"),
    path('categories/', views.categories, name="category"),
    path('category/<int:id>/<int:brand_id>', views.category_detail, name="category_detail")
]
