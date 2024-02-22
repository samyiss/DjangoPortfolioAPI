from rest_framework import generics

from .models import Gallery, Location
from .serializers import GallerySerializer, LocationSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render

class GalleryList(generics.ListCreateAPIView):
    serializer_class = GallerySerializer
    
    def get_queryset(self):
        queryset = Gallery.objects.all()
        return queryset


