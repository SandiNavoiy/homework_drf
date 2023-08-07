from rest_framework import viewsets

from Course.models import Course
from Course.serializers import CourseSerializer
from users.permissions import IsNotModerator, IsOwnerOrModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        """Переопределение метода get_permissions для назначение разных прав доступа на разные дейтсвия"""
        # создавать курсы может только пользователь, не входящий в группу модераторы
        if self.action == 'create':
            permission_classes = [IsNotModerator]
        # редактировать курсы может только создатель курса или модератор
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwnerOrModerator]

        # удалять курсы может только их создатель
        elif self.action == 'destroy':
            permission_classes = [IsOwner]

        return [permission() for permission in permission_classes]
