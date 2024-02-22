from rest_framework import serializers
from .models import Gallery, Location, Item

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('pictures', 'description', 'picture_date')        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model: Location
        fields = ['__all__']
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model: Item
        fields = ['__all__']
        
