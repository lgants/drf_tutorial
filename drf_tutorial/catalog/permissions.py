from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # SAFE_METHODS are GET, HEAD and OPTIONS; they're considered "safe" because they don't change any existing data
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
