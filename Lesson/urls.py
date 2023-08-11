from django.urls import path

from Lesson.apps import LessonConfig
from Lesson.views import (LessonCreateAPIView, LessonDestroyAPIView,
                          LessonListAPIView, LessonRetrieveAPIView,
                          LessonUpdateAPIView)

app_name = LessonConfig.name

urlpatterns = [
    path("create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("list/", LessonListAPIView.as_view(), name="lesson_list"),
    path("deteil/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_deteil"),
    path("update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
]
