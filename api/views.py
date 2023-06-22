from django.conf import settings
from django.urls import reverse
from product.models import Product
from cart.models import Cart


from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.views import APIView


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PlaceOrders(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = OrderSerializer
