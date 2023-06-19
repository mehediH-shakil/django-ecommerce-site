from django.contrib.auth import update_session_auth_hash
from PIL import Image
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, ChangePasswordForm, UserProfileForm
from .models import UserProfile
from product.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            birthday = form.cleaned_data['birthday']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            profile = UserProfile(user=user, first_name=first_name, last_name=last_name, email=email, birthday=birthday,
                                  gender=gender, address=address, phone=phone)
            profile.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    fields = []
    for field in user_profile._meta.fields:
        field_name = field.verbose_name.capitalize()
        field_value = getattr(user_profile, field.name)
        fields.append((field_name, field_value))

    context = {
        'fields': fields
    }
    return render(request, 'profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            # Check if the old password matches the user's current password
            if not request.user.check_password(old_password):
                messages.error(request, 'Incorrect old password.')
            # Check if the new password and confirmation match
            elif new_password != confirm_password:
                messages.error(request, 'Passwords do not match.')
            else:
                # Set the new password
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Password successfully changed.')
                return redirect('profile')
    else:
        form = ChangePasswordForm()

    context = {
        'form': form
    }
    return render(request, 'change_password.html', context)


@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'edit_profile.html', context)
