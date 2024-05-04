from django.db import models

from users.models import Profile


class Order(models.Model):
    CHOICES = (
        ('В работе', 'В работе'),
        ('Отменен', 'Отменен'),
        ('Доставлен', 'Доставлен'),
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Чей заказ")
    status = models.CharField(max_length=100, verbose_name="Статус заказа", choices=CHOICES)
    total_price = models.IntegerField(verbose_name="Стоимость заказа")
    order_date = models.DateField(verbose_name="Дата доставки", blank=True)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
