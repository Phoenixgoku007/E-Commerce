from django.db import models

# from account.models import ShopUser as User -> this will throw circular import error
from products.models import Products
from django.core.validators import MinValueValidator


class Cart(models.Model):
    """
    Cart class with user field which has a foreign key relationship with the ShopUser model.
    Inorder to avoid circular import issue instead of importing ShopUser model we are passing it as a string in user field.
    """

    user = models.ForeignKey("account.ShopUser", on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user


class CartItems(models.Model):
    """
    CartItems class with cart,product and quantity fields.
    Cart field has a foreignkey relationship with the cart model so all the fields in cartitems can be also accessed from cart model.
    MinvalueValidator is set to avoid setting product quantity to 0 in the cart.
    Default is 1 to avoid null value error in quantity.
    """

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)

    # def __str__(self):
    #    return self.cart
