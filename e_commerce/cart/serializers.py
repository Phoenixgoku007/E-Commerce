from rest_framework import serializers
from .models import Cart, CartItems

class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField() # serializer method field to define a variable in serializer field which is not present in the current model
    class Meta:
        model = CartItems
        fields = ['id','product','quantity','total_price']
    
    def get_total_price(self, cart_item:CartItems): # overriding the get_attribute method to get the values present in cartitem model
        return cart_item.quantity * cart_item.product.price
        

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
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id','user','items','grand_total']
    
    def get_grand_total(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())
        


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['quantity']


        
