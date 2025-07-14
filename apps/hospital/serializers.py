from rest_framework.serializers import ModelSerializer
from .models import Hospital
from apps.Address.models import Address
from apps.Address.serializers import Address_seriliaztion
from apps.users.serializers import UserSerializer
from apps.users.models import UserDetails,Role,UserRole,UserHospital
from apps.licenses.models import License
from apps.licenses.serializers import LicenseSerializer
from rest_framework import serializers


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
        
        if not address_id:
            raise serializers.ValidationError({"address": "Address ID is required in context."})
        if not license_id:
            raise serializers.ValidationError({"license": "License ID is required in context."})

        try:
            license = License.objects.get(id=license_id)
        except License.DoesNotExist:
            raise serializers.ValidationError({"license": "License not found."})

        try:
            address = Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            raise serializers.ValidationError({"address": "Address not found."})

        validated_data.pop("address", None)
        validated_data.pop("license", None)

        hospital,_= Hospital.objects.get_or_create(
            owner=request.user,
            address=address,
            license=license,
            **validated_data
        )

        role = Role.objects.filter(name='Hospital Director').first()
    
        if not role:
            raise ValueError("Role 'Hospital Director' does not exist.")
        
        userrole, _ = UserRole.objects.get_or_create(user=request.user, defaults={"role": role})
        userhospital, _ = UserHospital.objects.get_or_create(user=request.user, defaults={"hospital": hospital})

        
        UserDetails.objects.get_or_create(
        user_obj=request.user,
        defaults={
            "address": address,
            "role": userrole,
            "hospital": userhospital,
            "reporting_to": request.user,
        }
        )
        
        return hospital
            

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
