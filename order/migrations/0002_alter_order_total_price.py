# Generated by Django 5.0.4 on 2024-05-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(verbose_name='Стоимость заказа'),
        ),
    ]
