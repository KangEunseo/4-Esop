from django.contrib import admin
from django.urls import path, include

app_name = 'shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]
