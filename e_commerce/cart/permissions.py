from rest_framework.permissions import BasePermission
from account.models import ShopUser


class CartPermission(BasePermission):
    """
    Cartpermission class which checks if the user is authenticated or not.
    If authenticated allow the logged in customer to perfrom get,put,patch and post operations.
    """

    def has_permission(self, request, view):
        """
        Function to check if the user is logged-in and has the role of Customer
        """
        if not request.user.is_authenticated:
            return False
        else:
            if request.user.role == ShopUser.CUSTOMER:
                return True
