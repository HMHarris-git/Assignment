from django.urls import path
from .views import ListCategory, ListProduct, DetailCategory, DetailProduct

# creating urls for routing through the api.

urlpatterns =[
    path('categories/', ListCategory.as_view(), name='all_categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='single_category'),
    path('products/', ListProduct.as_view(), name='all_products'),
    path('products/<int:pk>', DetailProduct.as_view(), name='single_product'),
]