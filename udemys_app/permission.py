from rest_framework.permissions import BasePermission


class CheckStatusPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'student'


class CreateCoursePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'teacher'