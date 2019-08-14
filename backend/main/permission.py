from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return obj.user == request.user
        except AttributeError:
            return obj.reseller == request.user