from django.db import models
from cart.models import Cart

# Create your models here.


class Order(models.Model):
    """
    Order model with status options like pending and completed.
    cart field has an foreign key relationship with the Cart model and it can be accessed by the related name -> cart_items
    """

    PENDING = "P"
    COMPLETED = "C"

    ROLE_CHOICES = [(PENDING, "Pending"), (COMPLETED, "Completed")]

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    status = models.CharField(max_length=10, choices=ROLE_CHOICES, default=PENDING)
