from django.db import models
from django.conf import settings

from blog.models import *

# Create your models here.

User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             on_delete=models.SET_NULL,
                             blank=True)
    product = {
        models.OneToOneField(Product_TV,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True),
        models.OneToOneField(Product_Phone,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True),
        models.OneToOneField(Product_a_laptop,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True),
    }
    boolean = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return "{}".format(self.product.title)


class Cart(models.Model):
    product = {
        models.ManyToManyField(Product_TV, null=True, blank=True),
        models.ManyToManyField(Product_Phone, null=True, blank=True),
        models.ManyToManyField(Product_a_laptop, null=True, blank=True)
    }
    cartitem = models.ManyToManyField(CartItem,
                                      blank=True,
                                      related_name='itemcart')
    decimal = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_ordered = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}" (self.id)
