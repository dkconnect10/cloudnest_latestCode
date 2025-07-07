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