from django import template

register = template.Library()


@register.filter
def get_discount_price(price, discount):
    return price - (price * (discount * 0.01))
