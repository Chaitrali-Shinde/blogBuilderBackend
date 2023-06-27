from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.http import JsonResponse
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Create your views here.

def allBlogPost(request):
    blogPosts= Post.objects.all()  #this query tell the DB to give all the objects
    output= ",". join([p.title for p in blogPosts])
    return JsonResponse(output,  safe=False)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'content', 'author','createdAt']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer