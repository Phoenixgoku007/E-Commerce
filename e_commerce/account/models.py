from django.db import models
from django.contrib.auth.models import AbstractUser
from cart.models import Cart

# Create your models here.


class ShopUser(AbstractUser):
    """
    Class to create a Customer user model which inherits all the properties of AbstractUser Model.
    Only the role field is getting overriden to the model.
    get_cart method either returns or creates an cart object and can be accessed through out the project
    """

    ADMIN = "A"
    STAFF = "S"
    CUSTOMER = "C"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (STAFF, "Staff"),
        (CUSTOMER, "Customer"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)

    def get_cart(self):
        """
        get_cart is a custom function defined in the user model
        so that it can be accessed from any other sections like cart,order or payment easily in a structured way.
        If the user already has an cart it just returns it or it will create an cart for the user and then returns it.
        """
        try:
            cart = Cart.objects.get(user=self)
        except Cart.DoesNotExist:
            cart = Cart(user=self)
            cart.save()

        return cart
