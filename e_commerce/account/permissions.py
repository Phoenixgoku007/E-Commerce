from rest_framework.permissions import BasePermission
from .models import ShopUser

class RolePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return (
            request.user.role == ShopUser.ADMIN or
            request.user.role == ShopUser.STAFF and request.method in ('GET','PUT','PATCH') or
            request.user.role == ShopUser.CUSTOMER and request.method in ('GET', 'HEAD', 'OPTIONS')
        )
