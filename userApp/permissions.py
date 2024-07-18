from rest_framework.permissions import BasePermission

class IsRegularUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'Regular':
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.id == obj.id