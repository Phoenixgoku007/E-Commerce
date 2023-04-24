from rest_framework import serializers
from .models import Cart, CartItems

class CartSerializer(serializers.Serializer):
    class Meta:
        model = Cart
        field = ['user']


class CartItemSerializer(serializers.Serializer):
    class Meta:
        model = CartItems
        field = ['cart','product','quantity']
