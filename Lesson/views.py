from rest_framework import generics

from Lesson.models import Lesson
from Lesson.serializers import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """Создание"""
    serializer_class = LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    """просмотр списка"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение элесента"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    """Изменение элемента"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление элемента"""
    queryset = Lesson.objects.all()