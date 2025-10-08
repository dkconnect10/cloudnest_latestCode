from rest_framework.serializers import ModelSerializer
from apps.patient.models import Patient
from apps.Address.serializers import AddressSerializer



class PatientSerializer(ModelSerializer):
    address = AddressSerializer(required = False)
    
    class Meta:
        model=Patient
        fields ='__all__'
        
    def create(self, validated_data):
        pass    