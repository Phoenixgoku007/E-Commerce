from django.db import models

class Payment(models.Model):
    payment_product = models.CharField(max_length=70)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=120)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payment_product
    