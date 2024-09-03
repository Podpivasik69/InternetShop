from django import forms
from .models import *

class PhoneForm(forms.Form):
    title = forms.CharField(max_length=25, label='Название')
    provider = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label='Выбери поставщика', label='Поставщик')
    model = forms.CharField(label='Модель')

    count_data = forms.CharField(label='Количество памяти')
    color = forms.CharField(label='Обложка')
    processor = forms.CharField(label='Процессор')
    camera = forms.CharField(label='Камера')
    battery = forms.CharField(label='Аккумулятор')

    price = forms.FloatField(label='Цена')
    photo = forms.ImageField(label='Фото')
