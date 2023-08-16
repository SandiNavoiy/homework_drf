from datetime import timedelta

from rest_framework import generics
from django.utils import timezone
from Lesson.models import Lesson
from Lesson.pagination import LessonPagination
from Lesson.serializers import LessonSerializer
from users.permissions import IsNotModerator, IsOwner, IsOwnerOrModerator
from Course.tasks import send_course_create, send_course_update


class LessonCreateAPIView(generics.CreateAPIView):
    """Создание урока"""

    serializer_class = LessonSerializer
    # permission_classes = [IsNotModerator]

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя созданному уроку"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()
        # Отправка на выполнение задачи при создании нового урока в курсе
        if new_lesson:
            send_course_create.delay(new_lesson.course.id)


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
    def perform_update(self, serializer):
        """Переопределение метода perform_create для добавления пользователя созданному уроку"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()
        # Отправка на выполнение задачи при изменении нового урока в курсе
        if new_lesson.course:
            new_lesson.course.last_updated = timezone.now()
            new_lesson.course.save()

            # Отправляем уведомление только если курс не обновлялся более 4 часов
        if new_lesson.course:
            send_course_update.delay(new_lesson.course.id)


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Удаление элемента - урока"""

    queryset = Lesson.objects.all()
    # permission_classes = [IsOwner]
