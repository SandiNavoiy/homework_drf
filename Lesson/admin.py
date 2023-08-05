from django.contrib import admin
from Lesson.models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', 'lesson_description')  # отображение на дисплее
    list_filter = ('lesson_name', 'lesson_description')  # фильтр
    search_fields = ('lesson_name', 'lesson_description')  # поля поиска

