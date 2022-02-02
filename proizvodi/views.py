from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
from .forms import PoductsForm

def product_create_view(request):
    form = PrductsForm(request.POST or None)
    if form.is_valid():
        form.save()


    context = {

        'form': form ,
    }
    return render(request, "proizvodi/proizvodi_create.html", context)

def product_detail_view(request):
    obj = Products.objects.get(id=1)
    obj2 = Products.objects.get(id=2)
    context = {
        # "title": obj.title,
        # "description": obj.description,

        'object': obj,
        'object2': obj2,
    }
    return render(request, "proizvodi/detail.html", context)
