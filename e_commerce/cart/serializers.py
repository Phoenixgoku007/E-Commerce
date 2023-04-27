from rest_framework import serializers
from .models import Cart, CartItems

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['id','product','quantity']

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        cart = self.context['cart']

        cart_item, created = CartItems.objects.get_or_create(product=product,cart=cart)

        if not created:
            cart_item.quantity +=quantity
            cart_item.save()
        else:
            cart_item.quantity=quantity
            cart_item.save()
        return cart_item


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True,read_only=True)

    class Meta:
        model = Cart
        fields = ['id','user','items']


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['quantity']
        
