from decimal import Decimal

from django.conf import settings

from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)  # self.session[settings.CART_ID]
        if not cart:
            cart = self.session[settings.CART_ID] = {}

        self.cart = cart

    def __str__(self):
        return self.cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):  # for문에서 하나씩 요소를 꺼낼 때 return값
        products_ids = self.cart.keys()

        products = Product.objects.filter(id__in=products_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product  # self.cart['0917']['product']

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self, product, quantity=1):  # cart에 product 추가
        pass

    def save(self):  # cart를 session에 저장
        pass

    def remove(self, product):  # cart에서 product 삭제
        pass

    def get_product_total(self):  # cart의 product 가격 합계
        pass
