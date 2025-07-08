from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.Address.models import Address
from .serializers import HospitalCreateSerializer, HospitalResponseSerializer
from apps.licenses.models import License
from django.db import transaction
from .swagger_docs.hospital_swagger import *
from rest_framework.parsers import MultiPartParser, FormParser
from apps.users.models import UserDetails
from .models import Hospital
from .serializers import HospitalCreateSerializer

class CreateHospital(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    @hospital_create_schema()
    def post(self, request):
        try:
            with transaction.atomic():
                user_instance = request.user

                required_fields = [
                    'name', 'email', 'phone', 'website',
                    'logo', 'established_year', 'Approval',
                    'address','city', 'state', 'country', 'pincode','license_number',
                    'issued_by','issue_date','expiry_date','document','is_verified'
                ]
                missing = [field for field in required_fields if not request.data.get(field)]
                if missing:
                    return Response({'error': f'Missing fields: {", ".join(missing)}'}, status=400)

                address,_ = Address.objects.get_or_create(
                    address=request.data.get('address'),
                    city=request.data.get('city'),
                    state=request.data.get('state'),
                    country=request.data.get('country'),
                    pincode=request.data.get('pincode'),
                )

                license_instance,_= License.objects.get_or_create(
                    license_number=request.data.get("license_number"),
                    defaults={
                    "issued_by":request.data.get('issued_by'),
                    "issue_date":request.data.get('issue_date'),
                    "expiry_date":request.data.get('expiry_date'),
                    "document":request.data.get('document'),
                    "is_verified":str(request.data.get('is_verified')).lower =='true'
                    }
                )
                hospital_data = {
                    "name": request.data.get('name'),
                    "email": request.data.get('email'),
                    "phone": request.data.get('phone'),
                    "website": request.data.get('website'),
                    "logo": request.data.get('logo'),
                    "established_year": request.data.get('established_year'),
                    "Approval": request.data.get('Approval'),
                    "address": address.id
                }

                serializer = HospitalCreateSerializer(
                            data=hospital_data,
                            context={"request": request, "address_id": address.id, 'license_id': license_instance.id}
                        )


                if serializer.is_valid():
                    user_instance.onboarding_complete = True
                    user_instance.save()
                    hospital = serializer.save()

                    
                    return Response({
                        "status": 200,
                        "message": "Hospital Register Successfully",
                        "Hospital": HospitalResponseSerializer(hospital).data
                    })

                return Response({"error": serializer.errors, "status": 400})

        except Exception as e:
            return Response({"error": str(e), "status": 501})

class Hospital_Users(APIView):
    permission_classes = [IsAuthenticated]
    @hospital_users_schema()
    def get(self, request):
        hospital_id = request.query_params.get('hospital_id')
        
        if not hospital_id:
            return Response({"message": "Hospital id is required", "status": 404}, status=404)
        
        userinfo = []
        userdetails = UserDetails.objects.select_related(
            'user_obj', 'address', 'role', 'hospital', 'reporting_to'
        ).filter(hospital=hospital_id)
        
        if userdetails:
            for user in userdetails:
                details = {
                    "full_name": user.user_obj.full_name if user.user_obj else None,
                    "address": (
                        f"{user.address.address}, {user.address.city}, {user.address.state}, {user.address.pincode}"
                        if user.address else None
                    ),
                    "role": user.role.name if user.role else None,
                    "hospital": user.hospital.name if user.hospital else None,
                    "reporting_to": user.reporting_to.full_name if user.reporting_to else None
                }
                userinfo.append(details)

        return Response({"User_Information": userinfo, "status": 200}, status=200)

class update_Hospital(APIView):
    permission_classes = [IsAuthenticated]

    @hospital_update_schema()
    def patch(self, request):
        hospital_id = request.query_params.get('hospital_id')
        if not hospital_id:
            return Response({"message": "hospital id is required", "status": 404}, status=404)

        try:
            hospital = Hospital.objects.get(id=hospital_id)
        except Hospital.DoesNotExist:
            return Response({"message": "Hospital not exist. Please create new hospital", "status": 401}, status=401)

        # Flatten fields
        data = request.data
        print("Request Data:", data)

        # Address update
        if hospital.address:
            address_instance = hospital.address
            address_instance.address = data.get('address', address_instance.address)
            address_instance.city = data.get('city', address_instance.city)
            address_instance.state = data.get('state', address_instance.state)
            address_instance.country = data.get('country', address_instance.country)
            address_instance.pincode = data.get('pincode', address_instance.pincode)
            address_instance.save()

        # License update
        if hospital.license:
            license_instance = hospital.license
            license_instance.license_number = data.get('license_number', license_instance.license_number)
            license_instance.issued_by = data.get('issued_by', license_instance.issued_by)
            license_instance.issue_date = data.get('issue_date', license_instance.issue_date)
            license_instance.expiry_date = data.get('expiry_date', license_instance.expiry_date)
            license_instance.document = data.get('document', license_instance.document)
            license_instance.is_verified = data.get('is_verified', license_instance.is_verified)
            license_instance.save()

        # Main hospital update
        update_fields = {
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "logo": data.get("logo"),
        }
        update_fields = {k: v for k, v in update_fields.items() if v is not None}

        serializer = HospitalCreateSerializer(hospital, data=update_fields, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Hospital updated successfully",
                "updated Data": serializer.data
            }, status=200)

        return Response({
            "message": "Something went wrong while updating Hospital details",
            "errors": serializer.errors,
            "status": 501
        }, status=501)
   
        
        
        
  
                
            
            
        
        
        