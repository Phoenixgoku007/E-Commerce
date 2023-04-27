from django.urls import path
from .views import CartView, CartUpdate

urlpatterns = [
    path('cartview/',CartView.as_view(),name='cartview'),
    path('cartupdate/<int:pk>/',CartUpdate.as_view(),name='cartupdate'),
    #path('cartupdate/<int:pk>/',CartUpdate.as_view(), name='cartupdate'),
]
