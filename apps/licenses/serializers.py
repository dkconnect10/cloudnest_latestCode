from rest_framework import serializers
from .models import License

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = [
            'id',
            'license_number',
            'issued_by',
            'issue_date',
            'expiry_date',
            'document',
            'is_verified',
            'remarks',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
