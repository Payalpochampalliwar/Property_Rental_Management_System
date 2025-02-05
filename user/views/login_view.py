from rest_framework.viewsets import ModelViewSet

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers import LoginSerializerValidator

class LoginView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializerValidator

    def login(self, request, *args, **kwagrs):
        email=request.data.get("email",None)
        password=request.data.get("password",None)
        serializer = LoginSerializerValidator(data=request.data)
        user = User.objects.get(email=email)
        if serializer.is_valid():
            login_user = authenticate(email=email, password=password)
            if login_user is None:
                return Response({"error" :"incorrect password or username"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error" :"username & password shouldn'\t be empty"}, status=400)
            
        token, _ = Token.objects.get_or_create(user=login_user)
        login_response={
            'id':user.id,
            'email':user.email,
            'username':user.username,
            'token': token.key
            }
            
        return Response({"success":"true","login response": login_response}, status=status.HTTP_200_OK)
