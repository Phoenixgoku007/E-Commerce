from django.shortcuts import render
from rest_framework import permissions
from .serializers import CartSerializer, CartItemSerializer, CartUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .permissions import CartPermission

# Create your views here.


class CartView(APIView):
    """
    CartView class to display the cart items and edit the cart items.
    """

    permission_classes = [CartPermission]

    def get(self, request):
        """
        Get method to fetch all the cart items by passing the cart object to cartserializer.
        serializer.data will print the values otherwise it will be in object form and will be difficult to understand
        """

        cart = (
            request.user.get_cart()
        )  # gets the cart object from the get_cart method present in user model
        serializer = CartSerializer(cart, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        """
        Post method to add new items to the cart or increasing the quantity of an particular item
        """

        cart = request.user.get_cart()
        context = {
            "cart": cart
        }  # for setting the cart id number automatically while creating a new cart
        serializer = CartItemSerializer(data=request.data, context=context)

        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartUpdate(APIView):
    """
    CartUpdate class to allow only the authenticated customers to update the quantity of the cart items.
    """

    permission_classes = [CartPermission]

    def put(self, request, pk):
        cart = request.user.get_cart()
        cart_item = cart.items.get(id=pk)
        serializer = CartUpdateSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data["quantity"]
            # if quantity <= 0:
            #     cart_item.delete()
            # else:
            #     cart_item.quantity = quantity
            cart_item.quantity = quantity
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
