from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from pay.models import Pay
from pay.pagination import PayPagination
from pay.serializers import PaySerializer


class PayCreateAPIView(generics.CreateAPIView):
    """Создание оплаты"""

    serializer_class = PaySerializer


class PayListAPIView(generics.ListAPIView):
    """Просмотр списка оплат"""

    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    pagination_class = PayPagination
    filter_backends = [SearchFilter, OrderingFilter]
    # Фильтры
    search_fields = ["payment_type", "course_name", "lesson_name"]
    # Сортировка прямая / обратная
    ordering_fields = ["pay_date"]
    ordering = ["-pay_date"]


class PayRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение элемента  - оплаты"""

    serializer_class = PaySerializer
    queryset = Pay.objects.all()


class PayUpdateAPIView(generics.UpdateAPIView):
    """Изменение элемента - оплаты"""

    serializer_class = PaySerializer
    queryset = Pay.objects.all()


class PayDestroyAPIView(generics.DestroyAPIView):
    """Удаление элемента  - оплаты"""

    queryset = Pay.objects.all()
