from django.db import models
from django.shortcuts import resolve_url


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('shop:product_in_category', self.slug)


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)    #100원, $9.99
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    image = models.ImageField(upload_to='products/%Y/%m/%d', default='products/no_image.jpg')
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']     #최신상품부터 보이게

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('shop:product_detail', self.id, self.slug)

