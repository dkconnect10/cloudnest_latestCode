# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
# from ..serializers import DoctorSerializer

# def doctor_create_schema():
#     return swagger_auto_schema(
#         operation_description="Create a doctor profile (along with license, address, and role setup)",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             required=[
#                 'specialization', 'experience_years', 'license_number',
#                 'issued_by', 'issue_date', 'expiry_date',
#                 'address', 'state', 'country', 'pincode', 'role'
#             ],
#             properties={
#                 'specialization': openapi.Schema(type=openapi.TYPE_STRING),
#                 'experience_years': openapi.Schema(type=openapi.TYPE_INTEGER),
#                 'license_number': openapi.Schema(type=openapi.TYPE_STRING),
#                 'issued_by': openapi.Schema(type=openapi.TYPE_STRING),
#                 'issue_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
#                 'expiry_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
#                 'document': openapi.Schema(type=openapi.TYPE_FILE, description="Upload license file"),
#                 'is_verified': openapi.Schema(type=openapi.TYPE_BOOLEAN),
#                 'address': openapi.Schema(type=openapi.TYPE_STRING),
#                 'state': openapi.Schema(type=openapi.TYPE_STRING),
#                 'country': openapi.Schema(type=openapi.TYPE_STRING),
#                 'pincode': openapi.Schema(type=openapi.TYPE_STRING),
#                 'role': openapi.Schema(type=openapi.TYPE_STRING, description="Example: 'Doctor'")
#             }
#         ),
#         responses={
#             201: openapi.Response("Doctor profile created successfully", DoctorSerializer),
#             400: "Bad Request - Missing/Invalid fields",
#             404: "Error creating doctor"
#         }
#     )
