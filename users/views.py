from rest_framework import viewsets

from users.models import User
from users.pagination import UserPagination
from users.serializers import UserSerializer, UserSerializerForOthers


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """Эндпоинт для подьзователей на модели viewsets.ModelViewSet"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination

    def get_serializer_class(self):
        """выбор класса сериализации"""
        try:
            if int(self.request.user.pk) == int(self.kwargs["pk"]):
                return UserSerializer
        except:
            return UserSerializerForOthers
