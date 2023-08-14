from rest_framework import generics

from Lesson.models import Lesson
from Lesson.pagination import LessonPagination
from Lesson.serializers import LessonSerializer
from users.permissions import IsNotModerator, IsOwner, IsOwnerOrModerator


class LessonCreateAPIView(generics.CreateAPIView):
    """Создание урока"""

    serializer_class = LessonSerializer
    # permission_classes = [IsNotModerator]

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя созданному уроку"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Просмотр списка уроков"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsOwnerOrModerator]
    pagination_class = LessonPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Отображение элемента  - урока"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsOwnerOrModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Изменение элемента урока"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    # permission_classes = [IsOwnerOrModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление элемента - урока"""

    queryset = Lesson.objects.all()
    # permission_classes = [IsOwner]
