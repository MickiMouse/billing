from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return bool(obj.user == request.user or request.user.is_superuser)
        except AttributeError:
            return bool(obj.reseller == request.user or request.user.is_superuser)
