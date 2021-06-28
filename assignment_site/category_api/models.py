from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create a Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        # Giving appropriate plural value for assigned name.
        verbose_name_plural = 'categories'      

# Creating a Product Model
class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ManyToManyField(Category, blank=True, related_name='product')
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name    