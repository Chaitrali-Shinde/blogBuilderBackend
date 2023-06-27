from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.http import JsonResponse

# Create your views here.

def allBlogPost(request):
    blogPosts= Post.objects.all()  #this query tell the DB to give all the objects
    output= ",". join([p.title for p in blogPosts])
    return JsonResponse(output,  safe=False)
