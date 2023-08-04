from rest_framework import serializers

from Course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    #добавление поля количество уроков  через описание нового типа, и сслыкой на запрос к лесссон, суммирование
    lessons_count = serializers.IntegerField(source='Lesson_set.all.count', read_only=True)
    #Добавднеие в сериализатор уроков для курса, смотри функцию get_lessons

    lessons = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons(self, instance):
        """Добавление уроков для курса"""
        lesson_list = []
        if instance.lesson_set.all():
            for i in instance.lesson_set.all().values_list():
                lesson_list.append(i[1])
            return lesson_list
        return None
