from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from serializers import UserSerializer

def register_or_verify_schema():
    return swagger_auto_schema(
        request_body=UserSerializer,  
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

def login_schema():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["email", "password"],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, format='email'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format='password'),
            }
        ),
        operation_description="Login using email and password",
        responses={
            200: openapi.Response("Login successful"),
            401: "Invalid credentials"
        }
    )

# Get Profile
def get_profile_schema():
    return swagger_auto_schema(
        operation_description="Fetch authenticated user profile",
        responses={200: openapi.Response("User profile", UserSerializer.updateUserserializer)}
    )

# Update Profile
def update_profile_schema():
    return swagger_auto_schema(
        request_body=UserSerializer.updateUserserializer,
        operation_description="Update authenticated user profile",
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="User ID", type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: "Profile updated",
            403: "Unauthorized",
            404: "User not found"
        }
    )

# Logout
def logout_schema():
    return swagger_auto_schema(
        operation_description="Logout the current user",
        responses={200: "Logout successful"}
    )

# Reset Password
def reset_password_schema():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["old_password", "new_password", "confirm_password"],
            properties={
                'old_password': openapi.Schema(type=openapi.TYPE_STRING),
                'new_password': openapi.Schema(type=openapi.TYPE_STRING),
                'confirm_password': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        operation_description="Reset password for authenticated user",
        responses={200: "Password updated", 400: "Invalid data"}
    )

# Forgot Password
def forgot_password_schema():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'uid': openapi.Schema(type=openapi.TYPE_STRING),
                'token': openapi.Schema(type=openapi.TYPE_STRING),
                'new_password': openapi.Schema(type=openapi.TYPE_STRING),
                'confirm_password': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        operation_description="Handle forgot password flow: 1st call sends email, 2nd resets password",
        responses={200: "Success", 400: "Invalid request"}
    )

# Account Deletion
def account_delete_schema():
    return swagger_auto_schema(
        operation_description="Soft delete the current user account",
        responses={200: "Account deleted"}
    )

# Deactivate / Reactivate
def account_toggle_schema():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["is_active"],
            properties={
                'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            }
        ),
        operation_description="Deactivate or Reactivate the account",
        responses={200: "Account state changed"}
    )
