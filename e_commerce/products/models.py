from django.db import models
from django.utils.text import slugify
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:

            self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)
    
    