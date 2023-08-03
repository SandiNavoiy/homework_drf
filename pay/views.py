from rest_framework import generics

from Lesson.serializers import LessonSerializer
from pay.models import Pay


class PayCreateAPIView(generics.CreateAPIView):
    """Создание"""
    serializer_class = LessonSerializer

class PayListAPIView(generics.ListAPIView):
    """просмотр списка"""
    serializer_class = LessonSerializer
    queryset = Pay.objects.all()

class PayRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение элесента"""
    serializer_class = LessonSerializer
    queryset = Pay.objects.all()

class PayUpdateAPIView(generics.UpdateAPIView):
    """Изменение элемента"""
    serializer_class = LessonSerializer
    queryset = Pay.objects.all()

class PayDestroyAPIView(generics.DestroyAPIView):
    """Удаление элемента"""
    queryset = Pay.objects.all()