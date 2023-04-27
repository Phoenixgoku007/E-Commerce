from django.shortcuts import render
from rest_framework import permissions
from .serializers import CartSerializer, CartItemSerializer,CartUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        cart = request.user.get_cart()
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    def post(self, request):
        
        cart = request.user.get_cart()
        context = {"cart" : cart}
        serializer = CartItemSerializer(data=request.data, context=context)

        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CartUpdate(APIView):
    permission_classes = [permissions.IsAuthenticated]
        
    def put(self, request, pk):
        cart = request.user.get_cart()
        cart_item = cart.items.get(id=pk)
        serializer = CartUpdateSerializer(cart_item,data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data['quantity']
            # if quantity <= 0:
            #     cart_item.delete()
            # else:
            #     cart_item.quantity = quantity
            cart_item.quantity = quantity
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

