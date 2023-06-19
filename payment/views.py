from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def checkout(request):
    return render(request, 'checkout.html')
