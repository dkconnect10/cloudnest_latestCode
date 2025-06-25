from .models import Doctor
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class Doctors(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        specialization=request.data.get('specialization')
        experience_years=request.data.get('experience_years')
        
        role=request.data.get('role')
        
        address=request.data.get('address')
        state=request.data.get('state')
        country=request.data.get('country')
        pincode=request.data.get('pincode')
        
        license_number=request.data.get('license_number')
        issued_by=request.data.get('issued_by')
        issue_date=request.data.get('issue_date')
        expiry_date=request.data.get('expiry_date')
        document=request.data.get('document')
        is_verified=request.data.get('is_verified')
        
        
        
        
        
        
        
        

