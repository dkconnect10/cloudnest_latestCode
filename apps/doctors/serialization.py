from .models import Doctor, License
from rest_framework.serializers import ModelSerializer
from users.serialization import RegisterUserSerializer, RoleSerializer
from Address.serialization import Address_seriliaztion


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
            'specialization',
            'user',
            'address',
            'role',
            'license',
            'experience_years'
        ]
