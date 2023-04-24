from django.urls import path
from .views import ProductViews
from rest_framework import routers

# '''urlpatterns = [
#     path('product-add/', ProductAdd.as_view(), name='product-add' ),
#     path('product-update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
#     path('product-update&delete/<int:pk>/', ProductUpdateDelete.as_view(), name='product-details'),
# ]'''

router = routers.DefaultRouter()
router.register('product', ProductViews, basename='product')

urlpatterns =router.urls
