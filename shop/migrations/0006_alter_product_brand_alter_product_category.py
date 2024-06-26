# Generated by Django 5.0.4 on 2024-04-30 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_brand_category_product_brand_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.brand', verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория'),
        ),
    ]
