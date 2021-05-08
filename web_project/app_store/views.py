from django.shortcuts import render
from .models import *
# Create your views here.

def store (request):

    products = Product.objects.all()
    category = Product_category.objects.all()
    return render(request,'app_store/store.html', {"products": products, "category": category})

def product_category (request, category_id):
    
    category = Product_category.objects.filter(id = category_id)
    product = Product.objects.filter(categorys__in = category)
    return render(request, "app_store/Product_category.html", {'category': category, 'products': product})