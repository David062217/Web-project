from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorys'
    

    def __str__(self):
        return self.name


class Post (models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=40)
    image = models.ImageField(upload_to = 'app_blog', null = True, blank = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    categorys = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
    

    def __str__(self):
        return self.title