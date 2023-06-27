from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
    author= models.CharField( max_length=100)
    createdAt= models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return model_to_dict(self)