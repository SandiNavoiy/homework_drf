from rest_framework import serializers

from Course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='Lesson_set.all.count', read_only=True)
    class Meta:
        model = Course
        fields = "__all__"
