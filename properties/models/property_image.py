from django.db import models
from .property import Property
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property/property_images/')
    name = models.CharField(max_length=255, blank=False, null=False)
    def __str__(self):
        return f"{self.property} - {self.name}"