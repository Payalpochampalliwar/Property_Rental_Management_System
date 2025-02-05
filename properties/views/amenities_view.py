from rest_framework import viewsets
from ..models import Amenity
from django_filters import rest_framework as filters
from ..filters import AmenityFilter
from ..serializers import AmenitySerializer

class AmenitiesViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    filter_backends = (filters.DjangoFilterBackend)
    filterset_class = AmenityFilter 
    
    
    

        
        
