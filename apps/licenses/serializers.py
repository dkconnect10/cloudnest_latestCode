from rest_framework import serializers
from .models import License

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = "__all__"
        read_only_fields = ['id', 'created_at', 'updated_at']
