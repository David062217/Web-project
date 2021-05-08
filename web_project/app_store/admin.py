from django.contrib import admin
from .models import *

# Register your models here.

class Product_category_admin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class Product_admin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Product_category, Product_category_admin)
admin.site.register(Product, Product_admin)