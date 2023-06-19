from rest_framework import serializers
from product.models import Product
from cart.models import Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
