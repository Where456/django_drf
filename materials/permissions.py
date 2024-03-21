from rest_framework import permissions
from users.models import UserRoles


class IsModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == UserRoles.MODERATOR


class IsCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsCourseOrLessonOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.course.author == request.user or obj.course.lesson_set.filter(author=request.user).exists()


class IsPaymentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user