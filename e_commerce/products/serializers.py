from rest_framework import serializers
from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    """
    ProductSerializer to serialize all the fields present in the Products model.
    Here I am making the slug field as read_only = True so that every time
    when adding a new product it will not be shown or ask for an value to be entered
    """

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Products
        fields = ("id", "name", "slug", "price", "description")
