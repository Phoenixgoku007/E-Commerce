from django.db import models
from django.contrib.auth.models import AbstractUser
from cart.models import Cart

# Create your models here.

class ShopUser(AbstractUser):
    
    ADMIN = 'A'
    STAFF = 'S'
    CUSTOMER = 'C'

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (STAFF, "Staff"),
        (CUSTOMER, "Customer"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)

    def get_cart(self):
        try:
            cart = Cart.objects.get(user=self)
        except Cart.DoesNotExist:
            cart = Cart(user=self)
            cart.save()
        
        return cart