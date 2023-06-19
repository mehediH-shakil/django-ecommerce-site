from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from paypal.standard.ipn import views as paypal_views
from store import views as user_views

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from paypal.standard.ipn import views as paypal_views
from store import views as user_views

from django.urls import include
from rest_framework import routers
from store.views import ProductView, OrderView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('change-password/', user_views.change_password, name='change-password'),
    path('edit-profile/', user_views.edit_profile, name='edit-profile'),

    path('products/', user_views.product_list, name='product_list'),
    path('cart/', user_views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/',
         user_views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/',
         user_views.remove_from_cart, name='remove_from_cart'),

    path('checkout/', user_views.checkout, name='checkout'),

    path('submit_review/<int:product_id>/',
         user_views.submit_review, name='submit_review'),
    path('product_detail/<int:product_id>/',
         user_views.product_detail, name='product_detail'),

    path('api/', include('rest_framework.urls')),
    path('api/products/', ProductView.as_view(), name='product-list'),
    path('api/orders/', OrderView.as_view(), name='order-create'),

]
