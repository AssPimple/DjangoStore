from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from products.models import ProductCategory, Product

# Create your views here.

def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'categories': ProductCategory.objects.all(),
        'object_list': Product.objects.all(),
    }
    return render(request,'products/products.html', context)
