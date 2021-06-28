from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# class-based views

# This will list all available categories as well as give an option to add a category.
class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    print(queryset)
    serializer_class = CategorySerializer

# This view will allow user to perform crud operation on a particular category.
class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    

# This will list all available categories as well as give an option to add a product.
class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# This view will allow user to perform crud operation on a particular product.
class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
