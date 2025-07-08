from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def hospital_create_schema():
    return swagger_auto_schema(
        operation_description="Create Hospital with nested address and license data (multipart/form-data)",
        manual_parameters=[
            # Hospital fields
            openapi.Parameter('name', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('email', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('phone', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('website', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('logo', openapi.IN_FORM, type=openapi.TYPE_FILE),
            openapi.Parameter('established_year', openapi.IN_FORM, type=openapi.TYPE_INTEGER),
            openapi.Parameter('Approval', openapi.IN_FORM, type=openapi.TYPE_STRING),

            # Address fields
            openapi.Parameter('address', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('city', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('state', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('country', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('pincode', openapi.IN_FORM, type=openapi.TYPE_INTEGER),

            # License fields
            openapi.Parameter('license_number', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('issued_by', openapi.IN_FORM, type=openapi.TYPE_STRING),
            openapi.Parameter('issue_date', openapi.IN_FORM, type=openapi.TYPE_STRING, format='date'),
            openapi.Parameter('expiry_date', openapi.IN_FORM, type=openapi.TYPE_STRING, format='date'),
            openapi.Parameter('document', openapi.IN_FORM, type=openapi.TYPE_FILE),
            openapi.Parameter(name='is_verified',in_=openapi.IN_FORM,type=openapi.TYPE_STRING,enum=['true', 'false'],
                            description="Pass 'true' or 'false' as string")
        ],
        responses={201: openapi.Response("Hospital created successfully")},
    )

def hospital_users_schema():
    return swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'hospital_id',
                openapi.IN_QUERY,
                description="ID of the hospital to fetch users from",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        operation_description="Get all users belonging to a specific hospital",
        responses={
            200: openapi.Response(
                description="List of user information",
                examples={
                    "application/json": {
                        "User_Information": [
                            {
                                "full_name": "Dr. John Doe",
                                "address": "123 Street, City, State, 123456",
                                "role": "Doctor",
                                "hospital": "City Hospital",
                                "reporting_to": "Dr. Jane Smith"
                            }
                        ],
                        "status": 200
                    }
                }
            ),
            404: "Hospital ID is required or no users found"
        }
    )
    
def hospital_update_schema():
    return swagger_auto_schema(
        operation_summary="Update a Hospital",
        operation_description="""
        Partially update hospital details including:
        - Basic info (name, email, phone, logo)
        - Nested address (address, city, state, country, pincode)
        - Nested license info (license_number, issued_by, issue_date, expiry_date, document, is_verified)
        Supports file uploads for `logo` and `license.document`.
        """,
        manual_parameters=[
            openapi.Parameter(
                name='hospital_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='ID of the hospital to update',
                required=True
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'hospital_details': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'email': openapi.Schema(type=openapi.TYPE_STRING),
                        'phone': openapi.Schema(type=openapi.TYPE_STRING),
                        'logo': openapi.Schema(type=openapi.TYPE_FILE),
                        'address': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'address': openapi.Schema(type=openapi.TYPE_STRING),
                                'city': openapi.Schema(type=openapi.TYPE_STRING),
                                'state': openapi.Schema(type=openapi.TYPE_STRING),
                                'country': openapi.Schema(type=openapi.TYPE_STRING),
                                'pincode': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        ),
                        'license': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'license_number': openapi.Schema(type=openapi.TYPE_STRING),
                                'issued_by': openapi.Schema(type=openapi.TYPE_STRING),
                                'issue_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                                'expiry_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                                'document': openapi.Schema(type=openapi.TYPE_FILE),
                                'is_verified': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                            }
                        )
                    }
                )
            },
            required=['hospital_details']
        ),
        consumes=['multipart/form-data'],
        responses={
            200: openapi.Response(description='Hospital updated successfully'),
            404: openapi.Response(description='Hospital ID is required'),
            401: openapi.Response(description='Hospital not found'),
            501: openapi.Response(description='Validation or update error'),
        }
    )
