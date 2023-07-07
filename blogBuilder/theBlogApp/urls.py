from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from django.http import JsonResponse


router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.allBlogPost, name= "allBlogPost")
]