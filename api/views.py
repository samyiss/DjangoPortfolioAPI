from rest_framework import generics

from .models import Gallery, Location
from .serializers import GallerySerializer, LocationSerializer

class GalleryList(generics.ListCreateAPIView):
    serializer_class =GallerySerializer
    
    def get_queryset(self):
        queryset = Gallery.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(picture_url=location)
            
        return queryset
