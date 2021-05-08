from django.shortcuts import render
from app_blog.models import *
# Create your views here.

def home(request):

    return render(request,'web_projectA/home.html')