from rest_framework import serializers
from ..models import PropertyImage

    
class PropertyImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    name = serializers.CharField(required=True)
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'name']