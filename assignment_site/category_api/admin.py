from category_api.models import Category
from django.contrib import admin
from .models import Category, Product

# Model Registration

admin.site.register(Category)
admin.site.register(Product)
