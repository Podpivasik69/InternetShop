from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


# Create your views here.
def home_index(request):
    return render(request=request, template_name='catalog/index.html')

def phone_list(request):
    context = {'all_phones': Phone.objects.all()}
    return render(request=request, template_name='catalog/phone/list.html', context=context)

def phone_description(request, phone_id):
    one_phone = get_object_or_404(Phone, pk=phone_id)
    return render(request=request, template_name='catalog/phone/info.html', context={'one_phone': one_phone})


def add_phone(request):
    global form
    if request.method=='POST':
        form=PhoneForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Phone.objects.create(** form.cleaned_data) #** для распаковки словаря, чтобы не писать title=title

    else:
        form = PhoneForm()
    return render(request, 'catalog/phone/add_phone.html', {'form':form})
