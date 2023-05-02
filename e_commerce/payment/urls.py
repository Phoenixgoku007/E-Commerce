from django.urls import path
from .views import start_payment, verify_payment

urlpatterns = [
    path("payment/", start_payment, name="payment"),
    path("payment_status/", verify_payment, name="payment_status"),
]
