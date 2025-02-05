from django.urls import path
from .views import PropertyViewSet,ImagePropertyView,AmenitiesViewSet


urlpatterns = [
    #property  Routing
    path('', PropertyViewSet.as_view({'get':'list','post':'create'}),name="properties"),
    path('edit/<int:pk>/', PropertyViewSet.as_view({'put':'update'}),name="edit-property"),
    path('delete/<int:pk>/', PropertyViewSet.as_view({'delete':'destroy'}),name="delete-property"),
    path('edit2/<int:pk>/', PropertyViewSet.as_view({'patch': 'partial_update'}), name="edit2-property"),
    path('<int:pk>/', PropertyViewSet.as_view({'get': 'retrieve'}), name="property"),

    #property Images Routing
    path('<int:property_id>/images/', ImagePropertyView.as_view({'post':'add'}), name='add-image'),
    path('<int:property_id>/images/<int:image_id>/', ImagePropertyView.as_view({'delete':'delete'}), name='delete-image'),

    #amenities Routing
    path('amenities', AmenitiesViewSet.as_view({'get':'list'}), name='list-amenities'),
   


]
