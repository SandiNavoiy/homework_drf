from django.contrib import admin

from Course.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_description')  # отображение на дисплее
    list_filter = ('course_name', 'course_description')  # фильтр
    search_fields = ('course_name', 'course_description')  # поля поиска

