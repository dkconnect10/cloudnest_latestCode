from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def register_or_verify_schema(serializer_class):
    return swagger_auto_schema(
        request_body=serializer_class,
        operation_description="Register a new user OR Verify user with uidb64 and token",
        manual_parameters=[
            openapi.Parameter('uidb64', openapi.IN_QUERY, description="Base64 encoded user ID", type=openapi.TYPE_STRING),
            openapi.Parameter('verifyed_token', openapi.IN_QUERY, description="Verification token", type=openapi.TYPE_STRING),
        ],
        responses={
            201: openapi.Response("User registered successfully"),
            202: openapi.Response("User verified successfully"),
            400: "Bad request",
            401: "Unauthorized",
            500: "Email sending failed"
        }
    )
