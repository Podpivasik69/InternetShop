from django.urls import path
from django.contrib import admin
from .views import (

    DeliveryListView,
    DeliveryCreateView,
    DeliveryUpdateView,
    DeliveryDeleteView,
    DeliveryDetailView,

)

urlpatterns = [
    # path('', DeliveryListView.as_view(), name='delivery_list'),

    path('', DeliveryListView.as_view(), name='deliveries'),

    path('<int:pk>/', DeliveryDetailView.as_view(), name='deliveries_detail'),
    path('new/', DeliveryCreateView.as_view(), name='deliveries_new'),
    path('<int:pk>/update/', DeliveryUpdateView.as_view(), name='deliveries_edit'),
    path('<int:pk>/delete/', DeliveryDeleteView.as_view(), name='deliveries_delete'),
]
