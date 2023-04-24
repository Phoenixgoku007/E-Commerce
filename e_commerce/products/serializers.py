from rest_framework import serializers
from products.models import Products

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Products
        fields = ('id','name','slug','price','description')
