from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.authentication import TokenAuthentication
from .serializers import ShopUserSerializer
from .models import ShopUser
from rest_framework.views import APIView

"""
RegisterUser class to register new users to our e-commerce module.
Permissions set to allow any so that any can register in our platform.
"""
class RegisterUser(generics.CreateAPIView):
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    permission_classes = [permissions.AllowAny]

"""
LoginUser class to login the registered users by sending a post request.
authenticate method returns the user object if the provided username and password are valid
login method uses the session id to login the current user and retains the session info
if the token is already present for the user it is getting returned or it will be created and returned in the response
"""
class LoginUser(generics.GenericAPIView):
    queryset = ShopUser.objects.all()
    serializer_class = ShopUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        username =serializer.validated_data.get('username') # only use get method if you are very sure that the values are being passed
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

        token, _ = Token.objects.get_or_create(user=user) # underscore is given to avoid receiving the boolean value received from get_or_create method that is True or false after checking token present or not

        response = {
            'success' : True,
            'token' : token.key,
            'statuscode' : status.HTTP_200_OK,
            'info' : 'User Loggin Successful',
            'username': username,
        }

        return Response(response)

"""
LogoutUser class logouts the current logged-in user by deleting the present token of the user.
Every time when the user login they have to provide a new token
The default expiry time of the auth token in django is infinite
"""
class LogoutUser(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self,request):
        token = request.auth
        token.delete()

        response = {
            'success':True,
            'statuscode':status.HTTP_200_OK,
            'Message':'Logged Out User Successfully',
        }

        return Response(response)
