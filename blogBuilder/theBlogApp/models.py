from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=500)
    content=models.CharField()
    author= models.CharField( max_length=100)
    createdAt= models.DateTimeField(auto_now_add=False)