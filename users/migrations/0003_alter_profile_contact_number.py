# Generated by Django 5.0.4 on 2024-05-01 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
