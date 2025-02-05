
from django.db import models
from user.models import User
from .amenities import Amenity
class Property(models.Model):
    description = models.TextField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)
    num_reviews = models.IntegerField(default=0)
    total_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    num_rooms = models.IntegerField()
    max_users = models.IntegerField()
    amenities = models.ManyToManyField(Amenity, blank=True)

    def avg_rating(self):
        return self.total_rating / self.num_reviews if self.num_reviews > 0 else 0
    def __str__(self):
        return self.description
