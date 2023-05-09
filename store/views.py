from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage ,PageNotAnInteger ,Paginator
from django.http import HttpResponse

from .models import Product
from carts.views import _cart_id
from category.models import Category
from carts.models import CartItem

import pdb





# Create your views here.

def store_page(request,cat_slug=None):
    
    categories = None
    prod = None
    
    if cat_slug!=None:
        categories = get_object_or_404(Category,category_slug =cat_slug)
        prod = Product.objects.filter(category = categories,is_available=True)
        paginator = Paginator(prod, 6)
        page = request.GET.get('page')
        paged_prod = paginator.get_page(page)
        prod_count = prod.count()
    else:
        prod = Product.objects.all().filter(is_available =True).order_by('id')
        paginator = Paginator(prod, 9) 
        page = request.GET.get('page')
        paged_prod = paginator.get_page(page)
        prod_count = prod.count()
    return render(request,'store.html',context={'products':paged_prod,'prod_count':prod_count})

def product_detail(request,cat_slug,prod_slug):
    try:
        single_product = Product.objects.get(category__category_slug = cat_slug,slug = prod_slug)
        in_cart =CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
        
    except Exception as e:
        raise e
    
    return render(request,'product_detail.html',context={'single_product':single_product,'in_cart':in_cart})

def search(request):
    
    prod =0
    if 'keyword' in request.GET:
        key = request.GET['keyword']
        if key:
            prod = Product.objects.order_by('-created_date').filter(product_name__icontains=key )
            prod_count = prod.count()

    return render(request,'store.html',context={'products':prod,'prod_count':prod_count})