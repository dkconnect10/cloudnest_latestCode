from .models import Doctor,License
from apps.users.models import UserDetails,Role
from apps.Address.models import Address
from rest_framework.views import APIView
from .permissions import IsDoctorOrAdmin
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response

class Doctors(APIView):
    permission_classes=[IsAdminUser]
    def post(self,request):
            specialization=request.data.get('specialization')
            experience_years=request.data.get('experience_years')
            
            user = request.user
            role_name=request.data.get('role','doctor')
            role = Role.objects.get(name__iexact=role_name)

            address=Address.objects.create(
                address=request.data.get('address'),
                state=request.data.get('state'),
                country=request.data.get('country'),
                pincode=request.data.get('pincode'),
            
            )
            existing_license = License.objects.filter(license_number=request.data.get('license_number')).first()
            if existing_license:
                return Response({'error': 'License with this number already exists'}, status=400)
            
            license=License.objects.create(
                license_number=request.data.get('license_number'),
                issued_by=request.data.get('issued_by'),
                issue_date=request.data.get('issue_date'),
                expiry_date=request.data.get('expiry_date'),
                document=request.data.get('document'),
                is_verified=request.data.get('is_verified',False) ,
            )
            
            if not UserDetails.objects.filter(user_obj=user).exists():
                UserDetails.objects.create(
                user_obj=user,
                role=role,
                address=address 
                )
                
            if Doctor.objects.filter(user=user).exists():
                return Response({'error': 'Doctor profile already exists'}, status=400) 
             
            Doctor.objects.create(
                user=user,
                specialization=specialization,
                address=address,
                role=role,
                license=license,
                experience_years=experience_years
            )
            return Response({'msg': 'Doctor profile created successfully'}, status=201)
        
            
        
        
        
        
        

