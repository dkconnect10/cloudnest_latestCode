from .models import Doctor
from rest_framework.serializers import ModelSerializer
from apps.users.serializers import UserSerializer , RoleSerializer
from apps.Address.serializers import Address_seriliaztion
from apps.licenses.serializers import LicenseSerializer


class DoctorSerializer(ModelSerializer):
    user = UserSerializer()
    address = Address_seriliaztion()
    role = RoleSerializer()
    license = LicenseSerializer()

    class Meta:
        model = Doctor
        fields = [
            'user',
            'address',
            'role',
            'specialization',
            'experience_years',
            'license',
            
        ]
