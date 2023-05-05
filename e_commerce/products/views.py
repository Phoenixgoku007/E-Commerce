from rest_framework import generics, permissions
from products.models import Products
from products.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from account.permissions import RolePermission


class ProductViews(ModelViewSet):
    """
    Product create,update,list,delete and retrive using ModelViewset
    """

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [RolePermission]


"""
The same above operations are done in the below code but using concrete view classes
"""

"""class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [RolePermission]
    role_required = ShopUser.CUSTOMER

class ProductAdd(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [RolePermission]
    role_required = ShopUser.STAFF or ShopUser.ADMIN

class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [RolePermission]
    role_required = ShopUser.STAFF or ShopUser.ADMIN

    def perform_update(self, serializer):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            serializer.save()
        else:
             raise PermissionError("You don't have permission to update product informations")

class ProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [RolePermission]
    role_required = ShopUser.ADMIN

    def perform_update(self, serializer):
        user = self.request.user
        if user.is_staff:
            serializer.save()
        elif user.is_superuser:
            serializer.save(created_by=user)
        else:
            raise PermissionError("You don't have permission to delete any products")"""
