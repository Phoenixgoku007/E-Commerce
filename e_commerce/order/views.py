from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from cart.serializers import CartSerializer
from rest_framework import status

# Create your views here.

class OrderView(APIView):
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart_obj = request.user.get_cart()
        order = cart_obj.cart_items.filter(status="Pending")
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            status =serializer.validated_data['status']

            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

