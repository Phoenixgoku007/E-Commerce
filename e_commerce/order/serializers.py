from .models import Order
from rest_framework import serializers
from cart.serializers import CartSerializer,CartItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only = True)
    class Meta:
        model = Order
        fields = ['id','status','cart_items']
    
    def create(self, validated_data):
        status = validated_data['status']
        order_items = Order.objects.get(status=status)
        return order_items

