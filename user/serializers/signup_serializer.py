from rest_framework import serializers
from ..models import User
from django.contrib.auth.password_validation import validate_password

class SginUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = (
            'email', 'username', 'full_name','user_gender','city','phone_number', 'password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True}
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
   
