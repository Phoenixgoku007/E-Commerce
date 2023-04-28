from .models import Order
from rest_framework import serializers
from cart.serializers import CartSerializer,CartItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only = True)
    cart_items = CartItemSerializer(many=True, read_only = True)
    class Meta:
        model = Order
        fields = ['id','status','cart','cart_items']

