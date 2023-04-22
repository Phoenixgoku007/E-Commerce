from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import ShopUser

class ShopUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        user = ShopUser.objects.create(
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
