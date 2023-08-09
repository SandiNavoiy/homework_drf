from rest_framework import serializers

from Lesson.models import Lesson
from Lesson.validators import LessonValidator


class LessonSerializer(serializers.ModelSerializer):
    """Сериалайзер"""
    validators = [LessonValidator(field='lesson_video_url')]  # Проверка валидности видео
    class Meta:
        model = Lesson
        fields = "__all__"
