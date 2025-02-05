
from ..serializers import SginUpSerializer
from rest_framework.generics import CreateAPIView
from ..models import User

class SignUpView(CreateAPIView):
    serializer_class=SginUpSerializer
    queryset=User.objects.all()
    