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
    @hospital_update_schema
    def patch(self, request):
        hospital_id = request.query_params.get('hospital_id')
        print("Hospital ID:", hospital_id)

        if not hospital_id:
            return Response({"message": "hospital id is required", "status": 404}, status=404)

        try:
            hospital = Hospital.objects.get(id=hospital_id)
        except Hospital.DoesNotExist:
            return Response({"message": "Hospital not exist. Please create new hospital", "status": 401}, status=401)

        hospital_data = request.data.get('hospital_details', {})
        hospitaladdress = hospital_data.get('address', None)
        hospitallicense = hospital_data.get('license', None)

    
        if hospitaladdress and hospital.address:
            try:
                address_instance = Address.objects.get(id=hospital.address.id)
                address_instance.address = hospitaladdress.get('address', address_instance.address)
                address_instance.city = hospitaladdress.get('city', address_instance.city)
                address_instance.state = hospitaladdress.get('state', address_instance.state)
                address_instance.country = hospitaladdress.get('country', address_instance.country)
                address_instance.pincode = hospitaladdress.get('pincode', address_instance.pincode)
                address_instance.save()
                print("Address updated successfully")
            except Exception as e:
                print("Address update failed:", e)

        if hospitallicense and hospital.license:
            try:
                license_instance = License.objects.get(id=hospital.license.id)
                license_instance.license_number = hospitallicense.get('license_number', license_instance.license_number)
                license_instance.issued_by = hospitallicense.get('issued_by', license_instance.issued_by)
                license_instance.issue_date = hospitallicense.get('issue_date', license_instance.issue_date)
                license_instance.expiry_date = hospitallicense.get('expiry_date', license_instance.expiry_date)
                license_instance.document = hospitallicense.get('document', license_instance.document)
                license_instance.is_verified = hospitallicense.get('is_verified', license_instance.is_verified)
                license_instance.save()
                print("License updated successfully")
            except Exception as e:
                print("License update failed:", e)

        hospital_data.pop('address', None)
        hospital_data.pop('license', None)

        serializer = HospitalCreateSerializer(hospital, data=hospital_data, partial=True)
        print("Serializer data:", hospital_data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Hospital updated successfully",
                "updated Data": serializer.data
            }, status=200)

        print("Hospital update error:", serializer.errors)
        return Response({
            "message": "Something went wrong while updating Hospital details",
            "errors": serializer.errors,
            "status": 501
        }, status=501)

        
        
        
        
  
                
            
            
        
        
        