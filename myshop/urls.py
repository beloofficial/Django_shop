from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls'),name='cart'),
    url(r'^coupons/', include('coupons.urls'), name='coupons'),
    url(r'^orders/', include('orders.urls'), name='orders'),
    url(r'^', include('shop.urls'),name='shop'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
