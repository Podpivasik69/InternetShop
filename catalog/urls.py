from django.urls import path, include

from catalog.views import *
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path('', views.home_index, name='home_index'),
    path('list/', views.phone_list, name='phone_list'),
    path('phone/<int:phone_id>',views.phone_description, name='phone_description'),
    path('phone/add_phone', add_phone, name='add_phone'),
    path('deliveries/', include('Delivery.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)