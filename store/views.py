from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.
def store_page(request,cat_slug=None):
    
    categories = None
    prod = None
    
    if cat_slug!=None:
        categories = get_object_or_404(Category,category_slug =cat_slug)
        prod = Product.objects.filter(category = categories,is_available=True)
        prod_count = prod.count()
    else:
        prod = Product.objects.all().filter(is_available =True)
        prod_count = prod.count()
    return render(request,'store.html',context={'products':prod,'prod_count':prod_count})

def product_detail(request,cat_slug,prod_slug):
    try:
        single_product = Product.objects.get(category__category_slug = cat_slug,slug = prod_slug)
    except Exception as e:
        raise e
    
    return render(request,'product_detail.html',context={'single_product':single_product})