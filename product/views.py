from django.contrib.auth import update_session_auth_hash
from PIL import Image
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.conf import settings
from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Product
import os


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)
