from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import ShopUserSerializer
from .models import ShopUser

class RegisterUser(generics.CreateAPIView):
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    permission_classes = [permissions.AllowAny]

class LoginUser(generics.GenericAPIView):
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        username =serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is None:
            raise serializers.ValidationError("User not present")
        
        try:
            login(request, user)
        except ValueError:
            raise serializer.ValidationError("Unable to loging with the given credentials")

        token, _ = Token.objects.get_or_create(user=user)

        response = {
            'success' : True,
            'token' : token.key,
            'statuscode' : status.HTTP_200_OK,
            'info' : 'User Loggin Successful',
            'username': username,
        }

        return Response(response, status=status.HTTP_200_OK)
