import decimal
from decimal import Decimal
from shop.models import Product


class Cart():
    """"""

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')

        if not cart:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'qty': quantity, 'price': str(product.price)}

        self.cart[product_id]['qty'] = quantity
        self.session.modified = True

    def get_total_price(self):
        sum_cart = 0
        for item in self.cart.values():
            if item['product'].discount > 0:
                sum_cart += decimal.Decimal((item['product'].price - (item['product'].price * (item['product'].discount * 0.01))) * item[
                    'qty'])
            else:
                sum_cart += decimal.Decimal(item['price'] * item['qty'])

        return sum_cart

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def update(self, product, quantity):
        if quantity <= 0:
            self.delete(product)
            return

        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = quantity
            self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item
