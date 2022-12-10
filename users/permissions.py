from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False


class ISAuthenticatedMovie(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True

        return False


class ISAuthenticatedUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User) -> bool:
        if request.user.id == obj.id or request.user.is_employee:
            return True
        
        
