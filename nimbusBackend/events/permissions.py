from rest_framework.permissions import BasePermission

from rest_framework.permissions import SAFE_METHODS

class IsOwnerOrReadonly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_staff \
                or obj.department == request.user.department:
            return True
        return False