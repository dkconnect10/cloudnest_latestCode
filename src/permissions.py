from rest_framework.permissions import BasePermission
from apps.users.models import UserDetails

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            userdetails = UserDetails.objects.get(user=request.user)
            return userdetails.role.name.lower() == 'admin'
        except UserDetails.DoesNotExist:
            return False
