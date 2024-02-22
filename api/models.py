from django.db import models
from django import forms


class Location(models.Model):
    locationName = models.CharField(max_length=100)

    def __str__(self):
        return self.locationName
    
    
    
class Item(models.Model):
    itemName = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.itemName
    
    
    
    
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class Pictures(models.Model):
    image = models.ImageField(upload_to='images/')

class Gallery(models.Model):
    pictures = models.FileField(upload_to='images/', blank=True, null=True)
    picture_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=100)
    picture_date = models.CharField(max_length=100)
    

