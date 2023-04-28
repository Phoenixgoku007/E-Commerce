from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from cart.serializers import CartSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class OrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        cart = request.user.get_cart()
        orders = cart.cart_items  # orders = cart.cart_items.filter(cart=cart,status=Order.PENDING)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        cart = request.user.get_cart()
        serializer = OrderSerializer(data=request.data, context={'cart':cart})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

