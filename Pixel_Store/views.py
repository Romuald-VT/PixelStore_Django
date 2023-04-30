from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def home(request):
    prod = Product.objects.all().filter(is_available =True)
    return render(request,'home.html',context={'products':prod})