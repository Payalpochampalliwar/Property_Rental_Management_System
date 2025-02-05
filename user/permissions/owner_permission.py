from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:return True #only get methods
        return obj.landlord == request.user # only owners can do edit/delete
