from django.contrib import admin
from .models import UserProfile, Product, Cart, Review

admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Review)
