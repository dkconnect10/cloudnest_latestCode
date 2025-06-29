from rest_framework.serializers import ModelSerializer
from .models import Hospital
from apps.users.serialization import RegisterUserSerializer
from apps.Address.serialization import Address_seriliaztion


class HospitalSerialization(ModelSerializer):
    owner = RegisterUserSerializer(read_only=True)
    address=Address_seriliaztion(read_only=True)
    class Meta:
        model= Hospital
        fields=['name','owner','email','phone','website','address','is_active']
        
       
   
