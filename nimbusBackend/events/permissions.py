from rest_framework.permissions import BasePermission

from events.models import Event

from rest_framework.generics import get_object_or_404

from rest_framework.permissions import SAFE_METHODS

class IsOwnerOrReadonly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or request.user.is_staff or obj.department == request.user.department