from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    # has_permission performs global permission check
    def has_permission(self, request, view):
        # SAFE_METHODS are GET, HEAD and OPTIONS; they're considered "safe" because they don't change any existing data
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff

class IsOwnerOrReadOnly(BasePermission):
    # has_object_permission performs object-level permission (e.g. only allow owners of an object to edit it)
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.created_by == request.user
