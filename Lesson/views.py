from rest_framework import generics

from Lesson.models import Lesson
from Lesson.pagination import LessonPagination
from Lesson.serializers import LessonSerializer
from users.permissions import IsNotModerator, IsOwner, IsOwnerOrModerator


class LessonCreateAPIView(generics.CreateAPIView):
    """Создание"""

    serializer_class = LessonSerializer
    # permission_classes = [IsNotModerator]

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя созданному уроку"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """просмотр списка"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsOwnerOrModerator]
    pagination_class = LessonPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение элемента"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Изменение элемента"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление элемента"""

    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]
