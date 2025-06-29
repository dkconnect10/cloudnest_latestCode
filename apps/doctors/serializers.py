from .models import Doctor, License
from rest_framework.serializers import ModelSerializer
from apps.users.serializers import RegisterUserSerializer , RoleSerializer
from apps.Address.serializers import Address_seriliaztion


class LicenseSerializer(ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'  


class DoctorSerializer(ModelSerializer):
    user = RegisterUserSerializer()
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
