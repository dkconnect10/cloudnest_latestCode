from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address', 'city', 'state', 'country', 'pincode', 'created_at', 'updated_at']

