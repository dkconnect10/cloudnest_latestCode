from rest_framework.serializers import ModelSerializer
from .models import Hospital
from apps.Address.models import Address
from apps.Address.serializers import Address_seriliaztion
from apps.users.serializers import UserSerializer
from apps.licenses.models import License
from apps.licenses.serializers import LicenseSerializer

class HospitalCreateSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = [
            'name', 'email', 'phone', 'website',
            'address', 'logo', 'established_year', 'Approval', 'license'  # singular
        ]

    def create(self, validated_data):
        request = self.context.get('request')
        address_id = self.context.get('address_id')
        license_id = self.context.get("license_id")
        license = License.objects.get(id=license_id)
        address = Address.objects.get(id=address_id)
        validated_data.pop("address", None)
        validated_data.pop("license", None)

        return Hospital.objects.create(
            owner=request.user,
            address=address,
            license=license,
            **validated_data
        )

class HospitalResponseSerializer(ModelSerializer):
    owner = UserSerializer()
    address = Address_seriliaztion()
    license=LicenseSerializer()

    class Meta:
        model = Hospital
        fields = [
            'name', 'email', 'owner', 'phone', 'website',
            'address', 'license','logo', 'established_year', 'Approval', 'is_active'
        ]
