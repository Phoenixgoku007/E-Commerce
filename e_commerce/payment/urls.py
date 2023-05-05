from django.urls import path
from .views import PaymentView, StartPayment, PaymentSuccess

urlpatterns = [
    path("payment/", StartPayment.as_view(), name="payment"),
    path("payment_page/", PaymentView.as_view(), name="payment_page"),
    path("payment_status/", PaymentSuccess.as_view(), name="payment_status"),
]
