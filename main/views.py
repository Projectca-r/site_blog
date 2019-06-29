from django.shortcuts import render

from .models import *

# Create your views here.

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    product_tv = cart_obj.product_tv.all()
    product_phone = cart_obj.product_phone.all()
    product_a_laptop = cart_obj.product_a_laptop.all()
    total = 0
    for x in product_tv,product_phone,product_a_laptop:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, 'main/home.html', {})