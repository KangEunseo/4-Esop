from django.shortcuts import render

from shop.models import Category, Product


def product_in_category(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'shop/list.html', {'categories': categories, 'products': products})