from django.urls import path
from django.conf import settings

from .views import *

urlpatterns = [
    path('', cart_home, name='cart'),
]