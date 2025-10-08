from rest_framework import serializers
from .models import Doctor, DoctorAvailability
from apps.Address.serializers import AddressSerializer
from apps.licenses.serializers import LicenseSerializer
from apps.Address.models import Address
from apps.licenses.models import License
from apps.hospital.serializers import HospitalSerializer
from apps.users.serializers import UserMiniSerializer
from apps.users.models import User
from apps.hospital.models import Hospital


class DoctorSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    license = LicenseSerializer(required=False)
    
   
    hospitals = serializers.PrimaryKeyRelatedField(
        queryset=Hospital.objects.all(),
        many=True,
        write_only=True,
        required=False
    )
    hospital_details = HospitalSerializer(source='hospitals', many=True, read_only=True)

  
    user = UserMiniSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='user',
        required=False
    )

    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        license_data = validated_data.pop('license', None)
        hospitals_data = validated_data.pop('hospitals', [])

        # Address & License
        address_obj = Address.objects.create(**address_data) if address_data else None
        license_obj = License.objects.create(**license_data) if license_data else None

        doctor = Doctor.objects.create(
            address=address_obj,
            license=license_obj,
            **validated_data
        )

        # Set hospitals
        if hospitals_data:
            doctor.hospitals.set(hospitals_data)

        return doctor

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        license_data = validated_data.pop('license', None)
        hospitals_data = validated_data.pop('hospitals', None)

        # Address update
        if address_data:
            if instance.address:
                for key, value in address_data.items():
                    setattr(instance.address, key, value)
                instance.address.save()
            else:
                instance.address = Address.objects.create(**address_data)

        # License update
        if license_data:
            if instance.license:
                for key, value in license_data.items():
                    setattr(instance.license, key, value)
                instance.license.save()
            else:
                instance.license = License.objects.create(**license_data)

        # Hospitals update
        if hospitals_data is not None:
            instance.hospitals.set(hospitals_data)

        # Other fields
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(read_only=True)
    
    class Meta:
        model = DoctorAvailability
        fields = '__all__'
        
    def validate(self, attrs):
        doctor = attrs.get('doctor')
        hospital = attrs.get('hospital')
        day_of_week = attrs.get('day_of_week')
        start_time = attrs.get('start_time')
        end_time = attrs.get('end_time')

        overlapping = DoctorAvailability.objects.filter(
            doctor=doctor,
            hospital=hospital,
            day_of_week=day_of_week,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exists()

        if overlapping:
            raise serializers.ValidationError("This time slot overlaps with an existing availability.")

        return attrs

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
