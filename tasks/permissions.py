from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Админ — полный доступ
    Владелец — доступ к своему объекту
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True          # админ может всё

        return obj.owner == request.user  # владелец
