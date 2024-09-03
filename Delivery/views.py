from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from django.shortcuts import render
from .forms import DeliveryForm

class DeliveryCreateView(CreateView):
    model = Deliveries
    form_class = DeliveryForm
    template_name = 'Deliveries/delivery_new.html'

    def form_valid(self, form):
        delivery_item = form.cleaned_data.get('delivery_item')
        if delivery_item:
            # Получаем цену выбранного телефона
            phone = Phone.objects.get(id=delivery_item.id)
            form.instance.delivery_price = phone.price
        else:
            form.instance.delivery_price = 0  # Если телефон не выбран, устанавливаем цену в 0
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        delivery_price = 0

        # Если форма уже отправлена, получаем выбранный телефон и его цену
        if self.request.POST:
            form = self.get_form(self.form_class)
            if form.is_valid():
                delivery_item = form.cleaned_data.get('delivery_item')
                if delivery_item:
                    phone = Phone.objects.get(id=delivery_item.id)
                    delivery_price = phone.price

        context['delivery_price'] = delivery_price
        return context



class DeliveryDetailView(DetailView):
    model = Deliveries
    form_class = DeliveryForm
    template_name = 'Deliveries/delivery_detail.html'

class DeliveryListView(ListView):
    model = Deliveries
    template_name = 'Deliveries/delivery_list.html'
    paginate_by = 3


class DeliveryUpdateView(UpdateView):
    model = Deliveries
    template_name = 'Deliveries/delivery_edit.html'
    form_class = DeliveryForm


class DeliveryDeleteView(DeleteView):
    model = Deliveries
    template_name = 'Deliveries/delivery_delete.html'
    success_url = reverse_lazy('delivery_list')
