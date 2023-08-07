from rest_framework import permissions


class IsUser(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        if obj in request.user.courses.all() or obj in request.user.lessons.all():
            return True
        return False