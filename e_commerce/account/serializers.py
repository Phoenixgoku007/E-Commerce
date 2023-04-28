from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import ShopUser


"""
ShopUserSerializer to serialize the values present in username and password field.
Overriding the create method to create an username and hash the entered password using set_password method
"""
class ShopUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100, write_only=True)
    
    def create(self, validated_data):
        user = ShopUser.objects.create(
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
