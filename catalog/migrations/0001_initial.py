# Generated by Django 5.0.7 on 2024-08-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telephon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('model', models.CharField(max_length=150, verbose_name='Модель')),
                ('count_data', models.CharField(blank=True, null=True, verbose_name='Количество памяти')),
                ('color', models.CharField(max_length=20, verbose_name='Цвет')),
                ('processor', models.CharField(blank=True, null=True, verbose_name='Процессор')),
                ('camera', models.CharField(blank=True, null=True, verbose_name='Камера')),
                ('battery', models.CharField(blank=True, null=True, verbose_name='Аккумулятор')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
        ),
    ]
