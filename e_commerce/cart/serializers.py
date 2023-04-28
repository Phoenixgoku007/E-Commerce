from rest_framework import serializers
from .models import Cart, CartItems

"""
CartItemSerializer class to serialize all the fields present in cartitem model and an extra field 
"""
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

"""
CartSerializer class to serialize all the fields present in cart model as well as some extra fields like items and grand_total.
items field is a nested serializer to cartitemserializer so that all the values in cartitemserializer will be present inside items.
since there is no field named grand_total in card model we are using serializermethodfield and overriding its get_attribute method with our requirments.
"""
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True,read_only=True)
    grand_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id','user','items','grand_total']
    
    def get_grand_total(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all()) # looping through all the items and getting the total price using the price*quantity formula and then finally returning the total sum using sum method.
        

"""
CartUpdateSerializer class to serialize only the quantity field while updating the quantity of cart items.
"""
class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['quantity']


        
