# Generated by Django 5.0.4 on 2024-05-03 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_brand_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='country',
            field=models.CharField(blank=True, choices=[('США', 'US'), ('Франция', 'FR'), ('Китай', 'CN'), ('Россия', 'RU'), ('Германия', 'GE'), ('Италия', 'IT'), ('Япония', 'JP')], max_length=100, verbose_name='Страна бренда'),
        ),
    ]
