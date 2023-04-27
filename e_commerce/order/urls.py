from django.urls import path
from .views import OrderView


urlpatterns = [
    path('orderview/',OrderView.as_view(),name='orderview'),
]
