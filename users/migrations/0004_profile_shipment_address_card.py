# Generated by Django 5.0.4 on 2024-05-04 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='shipment_address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Адресс доставки'),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_card', models.CharField(max_length=100, verbose_name='Имя владельца карты')),
                ('number_of_card', models.CharField(max_length=100, verbose_name='Номер карты')),
                ('expiration', models.CharField(max_length=100, verbose_name='Срок действия')),
                ('cvv', models.IntegerField(max_length=3, verbose_name='CVV код')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'verbose_name': 'Карта для оплаты',
                'verbose_name_plural': 'Карты для оплаты',
            },
        ),
    ]
