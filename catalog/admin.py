from django.contrib import admin
from .models import Phone, Company

class PhoneAdmin(admin.ModelAdmin):
     list_display = ('id', 'title', 'provider', 'model' ,
    'count_data','color','processor', 'price')
     list_display_links = ('id', 'model')
     search_fields = ('model',)

class CompanyAdmin(admin.ModelAdmin):
     list_display = ('id', 'title')
     list_display_links = ('id', 'title')
     search_fields = ('title',)


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Company, CompanyAdmin)


