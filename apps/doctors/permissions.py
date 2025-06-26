from rest_framework.permissions import BasePermission
from apps.users.models import UserDetails

class IsDoctorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            userdetails = UserDetails.objects.get(user=request.user)
            return userdetails.role.name.lower() in ['admin', 'doctor']
        except UserDetails.DoesNotExist:
            return False
