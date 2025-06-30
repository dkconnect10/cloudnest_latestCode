from .models import License
from rest_framework.serializers import ModelSerializer

class LicenseSerializer(ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'  