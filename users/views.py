
from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()