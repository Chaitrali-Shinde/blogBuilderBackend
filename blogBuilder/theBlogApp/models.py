from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
    author= models.CharField( max_length=100)
    createdAt= models.DateTimeField(auto_now_add=True)