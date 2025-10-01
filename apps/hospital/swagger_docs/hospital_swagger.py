from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from apps.users.serializers import UserSerializer

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
        This API partially updates the Hospital details.
        
        **Supports:**
        - Basic Info: `name`, `email`, `phone`, `logo` (file)
        - Address: `address`, `city`, `state`, `country`, `pincode`
        - License: `license_number`, `issued_by`, `issue_date`, `expiry_date`, `document` (file), `is_verified`
        
        🔐 Requires Auth Token  
        📎 Use `multipart/form-data` for file upload.
        """,
        manual_parameters=[
            openapi.Parameter(
                name='hospital_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=True,
                description='ID of the hospital to update'
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'phone': openapi.Schema(type=openapi.TYPE_STRING),
                'logo': openapi.Schema(type=openapi.TYPE_FILE),

                # Address fields
                'address': openapi.Schema(type=openapi.TYPE_STRING),
                'city': openapi.Schema(type=openapi.TYPE_STRING),
                'state': openapi.Schema(type=openapi.TYPE_STRING),
                'country': openapi.Schema(type=openapi.TYPE_STRING),
                'pincode': openapi.Schema(type=openapi.TYPE_STRING),

                # License fields
                'license_number': openapi.Schema(type=openapi.TYPE_STRING),
                'issued_by': openapi.Schema(type=openapi.TYPE_STRING),
                'issue_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'expiry_date': openapi.Schema(type=openapi.TYPE_STRING, format='date'),
                'document': openapi.Schema(type=openapi.TYPE_FILE),
                'is_verified': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            },
            required=[]  # All are optional for PATCH
        ),
        consumes=['multipart/form-data'],
        responses={
            200: openapi.Response(description='Hospital updated successfully'),
            404: openapi.Response(description='Hospital ID is required'),
            401: openapi.Response(description='Hospital not found'),
            501: openapi.Response(description='Validation or update error'),
        }
    )

def hospital_details_schema():
    return swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'hospital_id',
                openapi.IN_QUERY,
                description="ID of the hospital to fetch (Optional)",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        operation_description="Get a single hospital by ID or list of all hospitals if no ID is provided.",
        responses={
            200: openapi.Response(
                description="Hospital details or list",
                examples={
                    "application/json": {
                        "message": "Hospital fetched successfully",
                        "data": {
                            "id": 1,
                            "name": "City Care Hospital",
                            "email": "info@citycare.com",
                            "phone": "+91-9876543210",
                            "address": "123, Residency Road, Jaipur",
                            "city": "Jaipur",
                            "state": "Rajasthan",
                            "country": "India",
                            "pincode": "302001",
                            "license_number": "RJ-HSP-2024-00123",
                            "issued_by": "Health Dept",
                            "issue_date": "2025-07-08",
                            "expiry_date": "2030-07-08",
                            "is_verified": True
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="Hospital not found or invalid ID"
            ),
            500: openapi.Response(
                description="Internal server error"
            )
        }
    )

def register_or_verify_schema():
    return swagger_auto_schema(
        operation_summary="Register or Verify User",
        operation_description="Register a new user OR Verify email using uidb64 and token from query parameters.",
        request_body=UserSerializer,
        manual_parameters=[
            openapi.Parameter(
                name='uidb64',
                in_=openapi.IN_QUERY,
                description='Base64 encoded user ID',
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                name='verifyed_token',
                in_=openapi.IN_QUERY,
                description='Verification token for email',
                type=openapi.TYPE_STRING,
                required=False
            )
        ],
        responses={
            201: openapi.Response(description="User registered successfully"),
            202: openapi.Response(description="User verified successfully"),
            400: openapi.Response(description="Bad request"),
            401: openapi.Response(description="Unauthorized - Invalid token or user not found"),
            500: openapi.Response(description="Internal server error - Email sending failed"),
        }
    )

def assign_user_role_schema():
    """
    Swagger schema for AssignUserRole API
    Assign multiple roles to a single user.
    """
    return swagger_auto_schema(
        operation_summary="Assign Roles to User",
        operation_description="""
        Assign one or multiple roles to a specific user.
        
        - Provide `user_id` of the user
        - Provide `role_ids` as a list of role IDs to assign
        - Duplicate roles will be ignored automatically
        """,
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the user', example=4),
                'role_ids': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description='List of role IDs to assign',
                    example=[1, 2, 3]
                ),
            },
            required=['user_id', 'role_ids']
        ),
        responses={
            200: openapi.Response(
                description='Roles assigned successfully',
                examples={
                    "application/json": {
                        "message": "Roles assigned successfully",
                        "assigned_roles": [
                            {"user": "sajan", "role": "Admin"},
                            {"user": "sajan", "role": "Doctor"}
                        ]
                    }
                }
            ),
            404: openapi.Response(
                description='User not found or roles not found',
                examples={
                    "application/json": {"error": "User not found", "status": 404}
                }
            ),
            400: openapi.Response(
                description='Missing user_id or role_ids',
                examples={
                    "application/json": {"error": "missing user_id or role_ids", "status": 404}
                }
            ),
            500: openapi.Response(description='Internal server error')
        }
    )
