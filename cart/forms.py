from django import forms
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, reverse

from .models import *
from blog.models import (
    Product_TV,
    Product_Phone,
    Product_a_laptop,
)
