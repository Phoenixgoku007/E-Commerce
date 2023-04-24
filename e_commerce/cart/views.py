from django.shortcuts import render
from rest_framework import generics
from .serializers import CartSerializer, CartItemSerializer
from .models import Cart, CartItems
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemsViewSet(ModelViewSet):
    queryset = CartItems.objects.all()
    serializer_class = CartItemSerializer
