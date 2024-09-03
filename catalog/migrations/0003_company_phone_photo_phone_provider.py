# Generated by Django 5.0.7 on 2024-08-06 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_telephon_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Company')),
            ],
        ),
        migrations.AddField(
            model_name='phone',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='phone',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.company'),
        ),
    ]