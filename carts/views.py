from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from store.models import Product
from carts.models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def _cart_id(request):
    krt = request.session.session_key
    if not krt:
        krt = request.session.create()
    return krt

def add_cart(request,product_id):
    prod = Product.objects.get(id = product_id)
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product= prod,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=prod,quantity=1,cart=cart)
    
        cart_item.save()
    
   
    return redirect('cart')

def remove_cart(request,product_id):
    krt = Cart.objects.get(cart_id=_cart_id(request))
    prod = get_object_or_404(Product,id = product_id)
    krt_item = CartItem.objects.get(product=prod,cart=krt)
    if krt_item.quantity >1:
        krt_item.quantity -= 1
        krt_item.save()
    else:
        krt_item.delete()
    return redirect('cart')

def remove_cart_item(request,product_id):
    krt=Cart.objects.get(cart_id=_cart_id(request))
    prod =get_object_or_404(Product,id=product_id)
    krt_item = CartItem.objects.get(product=prod,cart=krt)
    krt_item.delete()
    
    return redirect('cart')

def cart_page(request,total=0,quantity=0,cart_item=None):
    
    tax=0
    grand_total=0
    try:
        krt = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.filter(cart=krt,is_active=True)
        for e in cart_item:
            total += (e.product.price*e.quantity)
            quantity += e.quantity
        tax = 0.05*total
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
            
    return render(request,'cart.html',context ={'total':total, 'quantity':quantity,'cart_item':cart_item,'tax':tax,'grand_total':grand_total})

