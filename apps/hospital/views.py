from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.Address.models import Address
from .serializers import HospitalCreateSerializer, HospitalResponseSerializer
from apps.licenses.models import License
from django.db import transaction
from .swagger_docs.hospital_swagger import hospital_create_schema

class CreateHospital(APIView):
    permission_classes = [IsAuthenticated]
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
                    "is_verified":request.data.get('is_verified')
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
