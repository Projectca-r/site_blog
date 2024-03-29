from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

from blog.models import *

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if User is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

class Item(models.Model):
    product_tv = models.ManyToManyField(Product_TV, null=True, blank=True)
    product_phone = models.ManyToManyField(Product_Phone, null=True, blank=True)
    product_a_laptop = models.ManyToManyField(Product_a_laptop, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product_tv = models.ManyToManyField(Product_TV, null=True, blank=True, related_name='cart_product')
    product_phone = models.ManyToManyField(Product_Phone, null=True, blank=True, related_name='cart_product')
    product_a_laptop = models.ManyToManyField(Product_a_laptop, null=True, blank=True, related_name='cart_product')
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

def m2m_changed_cart_receiver(sender, instance, action, *args, **kwergs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        product_tv = instance.product_tv.all()
        product_phone = instance.product_phone.all()
        product_a_laptop = instance.product_a_laptop.all()
        total = 0
        for x in product_tv, product_phone, product_a_laptop:
            total += x.price
        if instance.subtotal!= total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.product_tv.through)
m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.product_phone.through)
m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.product_a_laptop.through)


def pre_save_cart_receiver(sender, instance, *args, **kwergs):
    instance.total = instance.subtotal + 10

pre_save.connect(pre_save_cart_receiver, sender=Cart)