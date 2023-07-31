from rest_framework import viewsets

from Course.models import Course
from Course.serializers import CourseSerializer


class CourseViewSet(viewsets.ViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()