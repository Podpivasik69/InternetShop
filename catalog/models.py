from django.db import models

class Phone(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    provider = models.ForeignKey('Company', on_delete=models.PROTECT, null=True)
    model = models.CharField(max_length=150, verbose_name='Модель')
    # description = models.TextField(blank=True, null=True, verbose_name='Описание')

    count_data = models.CharField(blank=True, null=True, verbose_name='Количество памяти')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    processor = models.CharField(blank=True, null=True, verbose_name='Процессор')
    camera = models.CharField(blank=True, null=True, verbose_name='Камера')
    battery = models.CharField(blank=True, null=True, verbose_name='Аккумулятор')

    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='images/', null=True, verbose_name='Фото')

    def __str__(self):
        return f"{self.title} ({self.model})"
    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

class Company(models.Model):
    title = models.CharField(max_length=150, verbose_name='Company', db_index=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'



