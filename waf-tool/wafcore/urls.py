from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from .views import Configuration
default_router = routers.DefaultRouter()
default_router.register(r'configurations', Configuration, basename='configuration')
urlpatterns = [
    path('', include(default_router.urls)),
]