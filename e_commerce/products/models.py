from django.db import models
from django.utils.text import slugify
import random, string
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            try:
                self.slug = slugify(self.name)
                super(Products, self).save(*args, **kwargs)
            except:
                mixed_values = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=20))
                self.slug = slugify(self.name) + mixed_values
                super(Products, self).save(*args, **kwargs)
        super(Products, self).save(*args, **kwargs)
    
    