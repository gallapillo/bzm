from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.CharField(max_length=200, verbose_name="Описание категории", blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ["-name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя бренда")
    description = models.CharField(max_length=200, verbose_name="Описание бренда", blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        ordering = ["-name"]
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


# TODO: добавить валюту + Рейтинг и отзывы
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.IntegerField(verbose_name="Цена")
    description = models.CharField(max_length=200, verbose_name="Описание товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", blank=True,
                                    default=None, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд", blank=True, default=None,
                                 null=True)
    image = models.ImageField(blank=True, upload_to="product_images", verbose_name="Картинка товара")
    discount = models.IntegerField(default=0, verbose_name="Скидка")
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")
    draft = models.BooleanField(default=False, verbose_name="Черновик")

    def __str__(self) -> str:
        return f"Продукт {self.name} : Цена {self.price}"

    class Meta:
        ordering = ["-name"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
