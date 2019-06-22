from django import forms
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, reverse

from .models import *
from blog.models import (
    Product_TV,
    Product_Phone,
    Product_a_laptop,
)


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['cartitem', 'decimal']

    def save(self):
        product = get_object_or_404(
            {
                Product_TV,
                Product_Phone,
                Product_a_laptop,
            }, slug=slug)
        new_item = get_object_or_404(CartItem, product=product)
        new_cart = Cart.objects.create(
            cartitem=self.cleaned_data['cartitem'],
            decimal=self.cleaned_data['decimal'],
        )
        if new_item not in new_cart.itemcart.all():
            new_cart.itemcart.create(new_item)
            new_cart.save()
            return reverse('new_item')

        return new_cart