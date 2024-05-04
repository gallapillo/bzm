from django.contrib import admin
from django.urls import include, path
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('shop.urls')),
    path("users/", include('users.urls')),
    path("cart/", include('cart.urls')),
    path("order/", include('order.urls'))
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)