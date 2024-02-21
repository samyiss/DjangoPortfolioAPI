from django.db import models

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
    
    
    
class Gallery(models.Model):
    picture_url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    picture_date = models.CharField(max_length=100)
    
    def __str__(self):
        return self.picture_url