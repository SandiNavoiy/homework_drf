from rest_framework import generics

from Subscription.models import Subscription
from Subscription.pagination import SubscriptionPagination
from Subscription.serializers import SubscriptionSerializer


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Создание"""

    serializer_class = SubscriptionSerializer


class SubscriptionListAPIView(generics.ListAPIView):
    """просмотр списка"""

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    pagination_class = SubscriptionPagination


class SubscriptionRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение элемента"""

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    """Изменение элемента"""

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """Удаление элемента"""

    queryset = Subscription.objects.all()
