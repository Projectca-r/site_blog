from django.urls import path

from .views import *

urlpatterns = [
    path('', carts_list, name='cart_list_url'),
    path('cart/create/', CartCreate.as_view(), name='cart_create_url'),
    # path('add-to-cart/', add_to_cart, name = "add_to_cart"),
]