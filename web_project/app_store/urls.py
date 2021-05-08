from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name = 'store'),
    path('Product-category/int:<category_id>/', views.product_category, name = 'Product_category'),
]