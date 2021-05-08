from django.db import models

# Create your models here.

class Product_category (models.Model):
    name = models.CharField(max_length= 50)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name = "product_category"
        verbose_name_plural = "products_category"

    def __str__ (self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length= 50)
    categorys = models.ForeignKey(Product_category, on_delete= models.CASCADE)
    image = models.ImageField(upload_to= "store", null = True, blank = True)
    value = models.FloatField()
    availability = models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name