from django import forms
from .models import Deliveries
from catalog.models import Phone, Company


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Deliveries
        fields = ['delivery_number', 'delivery_data', 'provider', 'delivery_item', 'delivery_count',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Делаем поле только для чтения

        # Фильтруем поле delivery_item в зависимости от выбранного provider
        if 'provider' in self.data:
            try:
                provider_id = int(self.data.get('provider'))
                self.fields['delivery_item'].queryset = Phone.objects.filter(provider_id=provider_id)
            except (ValueError, TypeError):
                pass  # Обработка ошибок

    def clean(self):
        cleaned_data = super().clean()
        delivery_item = cleaned_data.get('delivery_item')

        if delivery_item:
            # Получаем цену телефона из модели Phone
            phone = Phone.objects.filter(id=delivery_item.id).first()
            if phone:
                cleaned_data['delivery_price'] = phone.price
            else:
                cleaned_data['delivery_price'] = 0  # Если телефон не найден, выставляем цену по умолчанию

        return cleaned_data