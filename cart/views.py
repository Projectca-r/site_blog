from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .models import *
from .forms import *

def carts_list(request):
    carts = Cart.objects.first()
    context = {
        'carts': carts,
    }
    return render(request, 'cart/cart_list.html', context=context)


class CartCreate(View):
    def get(self, request, slug):
        form = CartForm
        context = {
            'form': form,
        }
        return render(request, 'cart/cart_create.html', context=context)
