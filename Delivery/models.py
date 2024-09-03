from django.db import models
from catalog.models import Phone, Company
from django.urls import reverse
from datetime import date
class Deliveries(models.Model):
    delivery_number = models.CharField(max_length=255, verbose_name='Номер поставки')
    delivery_data = models.DateField(verbose_name='Дата поставки', default=date.today)
    provider = models.ForeignKey('catalog.Company', on_delete=models.CASCADE, )
    delivery_item = models.ForeignKey('catalog.Phone', on_delete=models.CASCADE, )
    delivery_price = models.FloatField(verbose_name='Цена')
    delivery_count = models.FloatField(default=1, verbose_name='Количество поставок')

    def __str__(self):
        return f"{self.delivery_item.title} - {self.provider.title}"
    def get_absolute_url(self):
        return reverse ('deliveries_detail', args=[str(self.pk)])
