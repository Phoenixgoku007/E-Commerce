from django.db import models
from account.models import ShopUser
from products.models import Products
from django.core.validators import MinValueValidator

# Create your models here.

class Cart(models.Model):
   user = models.ForeignKey(ShopUser,on_delete=models.CASCADE)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    
