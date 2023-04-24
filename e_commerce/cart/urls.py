from django.urls import path
from .views import CartViewSet, CartItemsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cart',CartViewSet, basename='cart')
router.register('cart',CartItemsViewSet, basename='cart')

urlpatterns =router.urls