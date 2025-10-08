from rest_framework import serializers
from .models import Hospital, UserHospital
from apps.users.models import User, Role, UserRole
from apps.Address.serializers import AddressSerializer
from apps.licenses.serializers import LicenseSerializer
from apps.Address.models import Address
from apps.licenses.models import License

class HospitalSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    license = LicenseSerializer(required=False)

    class Meta:
        model = Hospital
        fields = "__all__"
        read_only_fields = ['id', 'owner']

    def create(self, validated_data):
        address_data = validated_data.pop("address", None)
        license_data = validated_data.pop("license", None)

        # address create
        address_obj = None
        if address_data:
            address_obj = Address.objects.create(**address_data)

        # license create
        license_obj = None
        if license_data:
            license_obj = License.objects.create(**license_data)

        hospital = Hospital.objects.create(
            address=address_obj,
            license=license_obj,
            **validated_data
        )
        return hospital

class HospitalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHospital
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = UserRole
        fields = ['id', 'user', 'user_email', 'role', 'role_name']

class HospitalDetailSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True, source='users')

    class Meta:
        model = Hospital
        fields = '__all__'
