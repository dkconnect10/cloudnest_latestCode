from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def hospital_create_schema():
    return swagger_auto_schema(
        operation_description="Create hospital with inline Address and License details (no need to pass IDs)",
        manual_parameters=[],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                # HOSPITAL FIELDS
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING),
                'website': openapi.Schema(type=openapi.TYPE_STRING),
                'logo': openapi.Schema(type=openapi.TYPE_STRING, format='binary'),
                'established_year': openapi.Schema(type=openapi.TYPE_INTEGER),
                'Approval': openapi.Schema(type=openapi.TYPE_STRING),

                # ADDRESS FIELDS
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'city': openapi.Schema(type=openapi.TYPE_STRING),
                'state': openapi.Schema(type=openapi.TYPE_STRING),
                'country': openapi.Schema(type=openapi.TYPE_STRING),
                'pincode': openapi.Schema(type=openapi.TYPE_INTEGER),

                # LICENSE FIELDS
                'license_number': openapi.Schema(type=openapi.TYPE_STRING),
                'issued_by': openapi.Schema(type=openapi.TYPE_STRING),
                'issue_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'expiry_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'document': openapi.Schema(type=openapi.TYPE_STRING, format='binary'),
                'is_verified': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            },
            required=['name', 'email', 'phone', 'website', 'address', 'city', 'state', 'country', 'pincode', 'license_number', 'issued_by', 'issue_date', 'expiry_date']
        ),
        responses={
            201: openapi.Response("Hospital created successfully"),
            400: "Invalid input",
            401: "Unauthorized"
        }
    )
