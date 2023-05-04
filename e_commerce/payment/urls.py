from django.urls import path
from .views import PaymentView, payment_success, start_payment

urlpatterns = [
    path("payment/", start_payment, name="payment"),
    path("payment_page/", PaymentView.as_view(), name="payment_page"),
    path("payment_status/", payment_success, name="payment_status"),
]
