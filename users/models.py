from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='_profile_images')
    contact_number = models.CharField(blank=True, max_length=20)
    shipment_address = models.CharField(max_length=100, verbose_name="Адресс доставки", blank=True)

    def __str__(self) -> str:
        if self.contact_number:
            return f"{self.user.username} - {self.contact_number}"
        else:
            return f"{self.user.username}"


class Card(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name_of_card = models.CharField(max_length=100, verbose_name="Имя владельца карты")
    number_of_card = models.CharField(max_length=100, verbose_name="Номер карты")
    expiration = models.CharField(max_length=100, verbose_name="Срок действия")
    cvv = models.IntegerField(verbose_name="CVV код")

    class Meta:
        verbose_name = "Карта для оплаты"
        verbose_name_plural = "Карты для оплаты"
