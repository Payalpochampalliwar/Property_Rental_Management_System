from django.contrib import admin
from .models import Property,PropertyImage,Amenity

# Register your models here.
admin.site.register(PropertyImage)
admin.site.register(Property)
admin.site.register(Amenity)
