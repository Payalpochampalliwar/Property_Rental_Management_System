from django.db import models

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=250)

    def __str__(self):
        return self.name
