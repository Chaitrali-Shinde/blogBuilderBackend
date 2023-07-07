from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from .models import Post
from .serializers import PostSerializer

# Create your views here.
def allBlogPost(request):
    blogPosts = Post.objects.all()
    serializer = PostSerializer(blogPosts, many=True)
    return JsonResponse(serializer.data, safe=False)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
