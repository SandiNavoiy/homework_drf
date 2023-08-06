from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from pay.models import Pay
from pay.serializers import PaySerializer


class PayCreateAPIView(generics.CreateAPIView):
    """Создание"""
    serializer_class = PaySerializer

class PayListAPIView(generics.ListAPIView):
    """просмотр списка"""
    serializer_class = PaySerializer
    queryset = Pay.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    #Фильтры
    search_fields = ['payment_type', 'course_name', 'lesson_name']
    # Сортировка прямая / обратная
    ordering_fields = ['pay_date']
    ordering = ['-pay_date']

class PayRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение элесента"""
    serializer_class = PaySerializer
    queryset = Pay.objects.all()

class PayUpdateAPIView(generics.UpdateAPIView):
    """Изменение элемента"""
    serializer_class = PaySerializer
    queryset = Pay.objects.all()

class PayDestroyAPIView(generics.DestroyAPIView):
    """Удаление элемента"""
    queryset = Pay.objects.all()