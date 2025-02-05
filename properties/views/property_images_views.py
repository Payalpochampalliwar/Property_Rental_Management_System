from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Property, PropertyImage
from ..serializers import PropertyImageSerializer

class ImagePropertyView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertyImageSerializer
    def add(self, request, property_id):

        #check if there is a property or not
        try:
            property = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return Response({'error': 'property not found'}, status=404)

        #check if the request user is the owner
        if property.landlord != request.user:
            return Response({'error': 'You are not authorized to do'}, status=403)
        
        # u have to upload an image 
        image = request.FILES.get('image')
        caption = request.data.get('name', '')
        if not image:
            return Response({'error': 'No image provided u have to attach.'}, status=400)

        serializer = PropertyImageSerializer(data=request.data)
        if serializer.is_valid():
           PropertyImage.objects.create(property=property, image=image,name=caption)
           return Response({"success" :"imaged uploded"}, status=201)
        else:
            return Response({"error" :"image & name shouldn'\t be empty"}, status=400)
    
    def delete(self, request, property_id, image_id):
        #check if there is a property or not
        try:
            property = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return Response({'error': 'property not found'}, status=404)

        #check if the request user is the owner
        if property.landlord != request.user:
            return Response({'error': 'You are not authorized to do'}, status=403)
        
        
        try:
            property_image = PropertyImage.objects.get(id=image_id, property=property)
        except PropertyImage.DoesNotExist:
            return Response({'error': 'Image not found'}, status=404)

        property_image.delete()
        return Response({'success': 'Image deleted successfully'}, status=204)

        
        
