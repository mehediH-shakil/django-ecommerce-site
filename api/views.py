from django.conf import settings
from django.urls import reverse
from product.models import Product
from cart.models import Cart

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, OrderSerializer


class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PlaceOrders(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = OrderSerializer
