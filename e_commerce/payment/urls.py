from django.urls import path
from .views import start_payment

urlpatterns = [
    path('payment/',start_payment,name='payment'),
    #path('payment_status/',handle_payment_success,name='payment_status'),
]



