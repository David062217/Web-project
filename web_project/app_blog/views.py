from django.shortcuts import render
from app_blog.models import *
# Create your views here.

def blog (request):

    post = Post.objects.all()
    category = Category.objects.all()
    return render(request,'app_blog/blog.html', {'posts': post, 'category': category})

def category (request, category_id):
    
    category = Category.objects.filter(id = category_id)
    post = Post.objects.filter(categorys__in = category)
    return render(request, "app_blog/category.html", {'category': category, 'posts': post})