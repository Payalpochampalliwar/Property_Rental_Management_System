
from ..models import Amenity
import django_filters

class AmenityFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains',label="contains name")
    class Meta:
        model = Amenity
        fields = ['name' ] 

    
        

        

  

