from django.db import models
from django.contrib.auth.models import User

class Wallpaper(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

class WallpaperComments(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

class WallpaperCount(models.Model):
    comments = models.IntegerField()
    likes = models.IntegerField()
    views = models.IntegerField()




# Create your models here.
