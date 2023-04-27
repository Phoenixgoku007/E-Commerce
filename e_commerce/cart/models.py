from django.db import models
#from account.models import ShopUser as User
from products.models import Products
from django.core.validators import MinValueValidator

# Create your models here.

class Cart(models.Model):
   user = models.ForeignKey("account.ShopUser",on_delete=models.CASCADE)

   # def __str__(self):
   #     return self.user
   

class CartItems(models.Model):
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="items")
   product = models.ForeignKey(Products,on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)],default=1)

   # def __str__(self):
   #    return self.cart
    
    
    
    
