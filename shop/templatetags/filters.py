from django import template

register = template.Library()


@register.filter
def get_discount_price(price, discount):
    return price - (price * (discount * 0.01))


@register.filter
def get_full_qty_price(price, qty):
    return price * qty
