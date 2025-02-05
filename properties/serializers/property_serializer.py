from rest_framework import serializers
from ..models import Property,PropertyImage
from decimal import Decimal
from ..utility.earth_distance_calc import dist_calc
from .property_image_serializer import PropertyImageSerializer

class PropertySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField() 
    distance = serializers.SerializerMethodField()
    class Meta:
        model = Property
        fields = [
            'id', 'description', 'longitude', 'latitude', 'landlord', 'num_reviews', 'total_rating', 'price_per_night', 'num_rooms', 'max_users', 'avg_rating','distance','images','amenities'
        ]
        read_only_fields = ['num_reviews', 'total_rating', 'avg_rating', 'landlord','distance']  

        

    def get_avg_rating(self, obj):
        return obj.avg_rating() 

    # return the distance for each property 
    def get_distance(self, obj):
        # longitude & latitude
        user_longitude = self.context['request'].GET.get('longitude',None)
        user_latitude = self.context['request'].GET.get('latitude',None)

        if user_longitude and user_latitude:
            user_longitude = Decimal(user_longitude)
            user_latitude = Decimal(user_latitude)

            # custom func to calc the dist
            distance = dist_calc(user_latitude, user_longitude, obj.latitude, obj.longitude)
            return distance
        return None

    #list the properties images
    def get_images(self, obj):
        images = PropertyImage.objects.filter(property=obj)
        return PropertyImageSerializer(images, many=True).data