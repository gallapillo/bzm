from django.db import models

# TODO: Добавить категории + добавить валюту + еще что-нибудь
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.FloatField(verbose_name="Цена")
    description = models.CharField(max_length=200, verbose_name="Описание товара")
    discount = models.IntegerField(default=0, verbose_name="Скидка")
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")
    draft = models.BooleanField(default=False, verbose_name="Черновик")

