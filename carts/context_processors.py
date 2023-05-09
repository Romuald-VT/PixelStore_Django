from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    
    cart_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            krt = Cart.objects.filter(cart_id=_cart_id(request))
            krt_item =CartItem.objects.all().filter(cart=krt[:1])
            for e in krt_item:
                cart_count += e.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)    
        