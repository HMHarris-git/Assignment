from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Product

# Create Category Serializer
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        # Fields to be displayed in api.
        fields = (
            'id',
            'name',
        )

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'price',
            'stock',
        )