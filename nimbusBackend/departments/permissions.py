from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS


class IsAdminOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(IsAdminOrReadOnly, self).has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


class IsOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        is_owner = view.kwargs['pk'] == request.user.id or request.user.is_staff
        return request.method in SAFE_METHODS or is_owner
