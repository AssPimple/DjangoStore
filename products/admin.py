from django.contrib import admin
from products.models import Product, ProductCategory
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)