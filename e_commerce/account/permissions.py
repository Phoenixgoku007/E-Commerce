from rest_framework.permissions import BasePermission
from .models import ShopUser
from rest_framework.permissions import SAFE_METHODS


class RolePermission(BasePermission):
    """
    Rolepermission class which inherits all the properties of BasePermission and also I am overriding some new rules to it.
    Defining the necessary permission for ADMIN,STAFF and CUSTOMER
    """

    def has_permission(self, request, view):
        """
        If the user is not logged in they can not access the content.
        If the logged in user's role is admin they will have all the access permissions
        if the logged in user's role is staff they will have get,put and patch permissions
        if the logged in user's role is customer they will only have the basic permissions which are mentioned in SAFE_METHODS
        """
        if not request.user.is_authenticated:
            return False

        return (
            request.user.role == ShopUser.ADMIN
            or request.user.role == ShopUser.STAFF
            and request.method in ("GET", "PUT", "PATCH")
            or request.user.role == ShopUser.CUSTOMER
            and request.method in SAFE_METHODS
        )
