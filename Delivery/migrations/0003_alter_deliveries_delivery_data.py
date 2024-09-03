# Generated by Django 5.0.7 on 2024-09-03 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delivery', '0002_deliveries_delivery_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveries',
            name='delivery_data',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата поставки'),
        ),
    ]
