from django.db import models
from django.utils.text import slugify
import random, string


class Products(models.Model):
    """
    Products model with some necessary fields for creating the products with their name,price and description.
    Here in the slug field if the slug is already present I am adding some alphanumeric characters
    and then creating it so that slug field will always be unique.
    """

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Function to check if the slug field is already present
        if so it will add alphanumeric characters to the new slugfield and then creates it.
        For a product the slug field is generated only one time and it will not change every time we update the product name.
        """
        if not self.slug:
            try:
                self.slug = slugify(self.name)
                super(Products, self).save(*args, **kwargs)
            except:
                mixed_values = "".join(
                    random.choices(
                        string.ascii_lowercase + string.digits + string.ascii_uppercase,
                        k=20,
                    )
                )
                self.slug = slugify(self.name) + mixed_values
                super(Products, self).save(*args, **kwargs)
        super(Products, self).save(*args, **kwargs)
