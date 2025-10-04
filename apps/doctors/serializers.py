# apps/doctors/serializers.py
from rest_framework import serializers
from .models import Doctor
from apps.Address.serializers import AddressSerializer
from apps.licenses.serializers import LicenseSerializer
from apps.users.serializers import RoleSerializer

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)   # सिर्फ़ username/email दिखेगा
    address = AddressSerializer()
    license = LicenseSerializer()
    role = RoleSerializer()

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'specialization', 'experience_years', 'address', 'license', 'role']
