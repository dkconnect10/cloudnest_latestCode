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
from apps.users.serializers import UserSerializer
from apps.users.views import RegisterUser
from django.contrib.auth import get_user_model
from django.core.mail import send_mail  
from django.contrib.auth.tokens import PasswordResetTokenGenerator 
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from src.settings.base import  EMAIL_HOST_USER
from rest_framework import status

User = get_user_model()

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
   
class HospitalListOrDetailView(APIView):
    permission_classes=[IsAuthenticated]
    @hospital_details_schema()
    def get(self,request):
        hospital_id = request.query_params.get('hospital_id')
        try:
            if hospital_id:
                hospital_instance = Hospital.objects.filter(id=hospital_id).first()
                
                if hospital_instance:
                    serializer = HospitalResponseSerializer(hospital_instance)
                    return Response({"message":"Hospital Get successfully","Data":serializer.data},status=200)
                return Response({"message":"hospoital not found"},status=404)
            hospital_instance = Hospital.objects.all()
            serializer = HospitalResponseSerializer(hospital_instance,many=True)
            return Response({"message":"Hospitals fetched successfully","Data":serializer.data},status=200)
        except Exception as e :
            return Response({"error":str(e)},status=500)
            
class HospitalUserCreate(APIView):
    permission_classes = [IsAuthenticated]
    @register_or_verify_schema()
    def post(self, request):
        uidb64 = request.query_params.get('uidb64')
        verifyed_token = request.query_params.get('verifyed_token')

        try:
            if not uidb64 and not verifyed_token:
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()

                    email = serializer.validated_data.get("email")
                    user = User.objects.get(email=email)
                    token_generator = PasswordResetTokenGenerator()
                    token = token_generator.make_token(user)
                    uid = urlsafe_base64_encode(force_bytes(user.pk))

                    verify_link = f"http://localhost:3000/verify-email?uid={uid}&token={token}"
                    try:
                        send_mail(
                            subject='Verify your Email',
                            message=f"Click the link to verify your email:\n{verify_link}",
                            from_email=EMAIL_HOST_USER,
                            recipient_list=[email],
                            fail_silently=False,
                        )
                    except Exception as e:
                        return Response({"error": f"Failed to send email. Reason: {str(e)}"}, status=500)

                    return Response({"message": "User registered. Verification email sent.","token":token,"uid":uid}, status=201)
                else:
                    return Response(serializer.errors, status=400)

            
            if uidb64 and verifyed_token:
                try:
                    uid = force_str(urlsafe_base64_decode(uidb64))
                    user = User.objects.get(pk=uid)
                except (User.DoesNotExist, ValueError, TypeError):
                    return Response({"message": "User not found"}, status=status.HTTP_401_UNAUTHORIZED)

                token_generator = PasswordResetTokenGenerator()
                if not token_generator.check_token(user, verifyed_token):
                    return Response({"message": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)

                user.is_active = True
                user.is_email_verified = True
                user.save()
                return Response({"message": "User verified successfully"}, status=status.HTTP_202_ACCEPTED)

            return Response({"error": "Invalid request: either provide registration data or verification parameters"}, status=400)

        except Exception as e:
            return Response({"error": str(e)}, status=500)

class AssignUserRole(APIView):
    pass                             
                
            
            
        
        
        