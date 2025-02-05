from rest_framework import serializers
from ..models import Amenity
class AmenitySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    discription = serializers.CharField()
    class Meta:
        model = Amenity
        fields = ['id',  'name','discription']