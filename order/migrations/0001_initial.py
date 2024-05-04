# Generated by Django 5.0.4 on 2024-05-04 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_profile_shipment_address_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('В работе', 'В работе'), ('Отменен', 'Отменен'), ('Доставлен', 'Доставлен')], max_length=100, verbose_name='Статус заказа')),
                ('total_price', models.IntegerField(max_length=100, verbose_name='Стоимость заказа')),
                ('order_date', models.DateField(blank=True, verbose_name='Дата доставки')),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Чей заказ')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]