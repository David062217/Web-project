from django.shortcuts import render, redirect
from .shopping_cart import shopping_cart
from  app_store.models import *
# Create your views here.

def add_product (request, product_id):
    cart = shopping_cart(request)
    product = Product.objects.get(id = product_id)
    cart.add(product = product)

    return redirect("store")

def delete_product (request, product_id):
    cart = shopping_cart(request)
    product = Product.objects.get(id = product_id)
    cart.delete_product(product = product)

    return redirect("store")

def subtract_product (request, product_id):
    cart = shopping_cart(request)
    product = Product.objects.get(id = product_id)
    cart.subtract_product(product = product)

    return redirect("store")

def clear_cart(request, product_id):
    cart = shopping_cart(request)
    cart.clear_cart()

    return redirect("store")