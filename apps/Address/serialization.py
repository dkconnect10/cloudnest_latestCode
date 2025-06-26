from .models import Address
from rest_framework.serializers import ModelSerializer

class Address_seriliaztion(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
