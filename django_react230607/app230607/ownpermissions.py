from rest_framework import permissions

class ProfilePermission(permissions.BasePermission):

    def has_objecct_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHOD:
            return True
        return False