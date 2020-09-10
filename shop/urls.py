from django.urls import path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_in_category, name='product_all'),
    path('<category_slug>/', views.product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', views.product_detail, name='product_detail'),
]