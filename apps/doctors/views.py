from .models import Doctor,License
from apps.users.models import UserDetails,Role
from apps.Address.models import Address
from rest_framework.views import APIView
from .permissions import IsDoctorOrAdmin
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from .serializers import DoctorSerializer

class Doctors(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            required_fields=['specialization', 'experience_years', 'license_number', 'issued_by', 'issue_date', 'expiry_date', 'address', 'state', 'country', 'pincode', 'role']
            missing=[field for field in required_fields if not request.data.get(field)]
            
            if missing:
                return Response({'error': f'Missing fields: {", ".join(missing)}'}, status=400)
            
            specialization=request.data.get('specialization')
            experience_years=request.data.get('experience_years')
            
        
            user_instance = request.user
            role_name=request.data.get('role')
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
            
            if not UserDetails.objects.filter(user_obj=user_instance).exists():
                UserDetails.objects.create(
                user_obj=user_instance,
                role=role,
                address=address 
                )
                
            if Doctor.objects.filter(user=user_instance).exists():
                return Response({'error': 'Doctor profile already exists'}, status=400) 
             
            docter_details = Doctor.objects.create(
                user=user_instance,
                specialization=specialization,
                address=address,
                role=role,
                license=license,
                experience_years=experience_years
            )
            user_instance.onboarding_complete=True
            user_instance.save()
            return Response({'msg': 'Doctor profile created successfully',"Data":DoctorSerializer(docter_details).data}, status=201)
        except Exception as e:
            return Response({"error":str(e)},status=404)
            
        
            
        
        
        
        
        

