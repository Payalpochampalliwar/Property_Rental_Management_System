
from ..models import Property
from decimal import Decimal
import django_filters
from ..utility.earth_distance_calc import dist_calc
class LocationFilter(django_filters.FilterSet):
    longitude = django_filters.NumberFilter(field_name="longitude")
    latitude = django_filters.NumberFilter(field_name="latitude")
    max_price = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='lte',label="less than or equal")
    min_price = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='gt',label="greater than")
    distance = django_filters.NumberFilter( label="distance must be less than or equels with meters")
    # getting the longitude& latitude and filtering at point
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters.pop('longitude', None)
        self.filters.pop('latitude', None)
        self.filters.pop('distance', None)
    class Meta:
        model = Property
        fields = ['longitude', 'latitude' ] 

    def filter_queryset(self, queryset):
        longitude = self.request.GET.get('longitude')
        latitude = self.request.GET.get('latitude')
        distance = self.request.GET.get('distance')
        queryset = super().filter_queryset(queryset) 
        if longitude is  None or latitude is None:
            return queryset
        user_longitude = Decimal(longitude)
        user_latitude = Decimal(latitude)

        if distance is  None :distance=3000 # default
        else :distance =Decimal(distance)

        print(distance)
        filtered_queryset  = filter(lambda p: dist_calc(user_latitude, user_longitude, p.latitude, p.longitude) <= distance, queryset)
        return list(filtered_queryset )
    
        

        

  

