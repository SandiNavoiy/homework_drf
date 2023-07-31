from django.views import generic

from Lesson.models import Lesson
from Lesson.serializers import LessonSerializer


class LessonCreateAPIView(generic.CreateAPIView):
    """Создание"""
    serializer_class = LessonSerializer

class LessonListAPIView(generic.ListAPIView):
    """просмотр списка"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generic.RetrieveAPIView):
    """Отображение элесента"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generic.UpdateAPIView):
    """Изменение элемента"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generic.DestroyAPIView):
    """Удаление элемента"""
    queryset = Lesson.objects.all()