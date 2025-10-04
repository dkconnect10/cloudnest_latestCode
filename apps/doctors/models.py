# apps/doctors/models.py
from django.db import models
from apps.users.models import User
from apps.Address.models import Address
from apps.licenses.models import License
from apps.users.models import Role

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_profiles")
    specialization = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField(default=0)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    license = models.OneToOneField(License, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.specialization}"
