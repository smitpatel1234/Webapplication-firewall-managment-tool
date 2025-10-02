from django.shortcuts import render
from django.http import JsonResponse
from .models import Configuration
from rest_framework.viewsets import ModelViewSet
from .serializers import ConfigurationSerializer
# Create your views here.
class Configuration(ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
