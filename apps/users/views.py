from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import User
from .serializers import UserSerializer, updateUserserializer,GetAllUserSerializer
from src.settings.base import EMAIL_HOST_USER
from .tasks import userActivation_Task
from apps.users.swagger_docs.user_swagger import *
from rest_framework.generics import ListAPIView
# from rest_framework.pagination import PageNumberPagination
from .pagination import MyCursorPagination




class RegisterUser(APIView):
    @register_or_verify_schema()
    def post(self, request):
        uidb64 = request.query_params.get('uidb64')
        token = request.query_params.get('verifyed_token')

        if uidb64 and token:
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (User.DoesNotExist, ValueError, TypeError):
                return Response({"message": "User not registered"}, status=status.HTTP_401_UNAUTHORIZED)

            token_generator = PasswordResetTokenGenerator()
            if not token_generator.check_token(user, token):
                return Response({"message": "Token not valid. Please register again"}, status=status.HTTP_401_UNAUTHORIZED)

            user.is_active = True
            user.is_email_verified = True
            user.save()
            return Response({"message": "User verified successfully"}, status=status.HTTP_202_ACCEPTED)

        # Normal registration
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()

            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            verify_link = f"http://localhost:3000/verify-email?uid={uid}&token={token}"
            try:
                send_mail(
                    subject='Verify your Email',
                    message=f"Click to verify: {verify_link}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
            except Exception as e:
                return Response({"error": f"Failed to send email: {str(e)}"}, status=500)

            return Response({"message": "User registered successfully", "token": token, "uid": uid}, status=status.HTTP_201_CREATED)

        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class loginUser(APIView):
    @login_schema()
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "status": 201,
                "message": "User logged in successfully",
                "user": user.username,
                "access_token": str(refresh.access_token)
            })
        return Response({"error": "Invalid Credentials", "status": 401})

class GetProfile(APIView):
    permission_classes = [IsAuthenticated]
    @get_profile_schema()
    def get(self, request):
        serializer = updateUserserializer(request.user)
        return Response(serializer.data)

class UpdateProfile(APIView):
    permission_classes = [IsAuthenticated]
    @update_profile_schema()
    def patch(self, request, pk):
        try:
            user_to_update = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=404)

        if request.user != user_to_update and not request.user.is_superuser:
            return Response({"message": "Not authorized"}, status=403)

        serializer = updateUserserializer(user_to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully"})
        return Response({"error": serializer.errors}, status=400)

class logoutUser(APIView):
    permission_classes = [IsAuthenticated]
    @logout_schema()
    def post(self, request):
        logout(request)
        return Response({"message": "User logged out successfully"})

class ResetPassword(APIView):
    permission_classes = [IsAuthenticated]
    @reset_password_schema()
    def post(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        user = request.user

        if not all([old_password, new_password, confirm_password]):
            return Response({"message": "All fields required"}, status=400)
        if new_password != confirm_password:
            return Response({"message": "Password mismatch"}, status=400)
        if not check_password(old_password, user.password):
            return Response({"message": "Old password is incorrect"}, status=400)

        user.set_password(new_password)
        user.save()
        return Response({"message": "Password updated successfully"})

class forgotPassword(APIView):
    @forgot_password_schema()
    def post(self, request):
        email = request.data.get('email')
        uidb64 = request.data.get('uid')
        token = request.data.get('token')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if email and not (uidb64 and token):
            user = User.objects.filter(email=email).first()
            if not user:
                return Response({"message": "Email not registered"}, status=404)

            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"http://yourdomain.com/reset-password?uid={uid}&token={token}"

            try:
                send_mail(
                    subject='Reset Password',
                    message=f"Click to reset: {reset_link}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
            except Exception as e:
                return Response({"error": f"Email send failed: {str(e)}"}, status=500)

            return Response({"message": "Reset link sent", "token": token, "uid": uid})

        elif uidb64 and token and new_password and confirm_password:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.filter(pk=uid).first()
            if not user:
                return Response({"message": "User not registered"}, status=401)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({"message": "Token invalid"}, status=401)

            if new_password != confirm_password:
                return Response({"message": "Password mismatch"}, status=400)

            user.set_password(new_password)
            user.save()
            return Response({"message": "Password reset successfully"})

        return Response({"error": "Invalid request"}, status=400)

class AccountDeletion(APIView):
    permission_classes = [IsAuthenticated]
    @account_delete_schema()
    def post(self, request):
        user = request.user
        if not user.is_active:
            return Response({"message": "User already deleted"}, status=400)

        user.is_active = False
        user.save()
        return Response({"message": "Account deleted successfully"})

class AccountDeactivationReactivation(APIView):
    permission_classes = [IsAuthenticated]
    @account_toggle_schema()
    def post(self, request):
        is_active = request.data.get('is_active')
        if is_active is None:
            return Response({"error": "'is_active' required"}, status=400)

        user = request.user
        if user.is_active == is_active:
            state = "already active" if is_active else "already deactivated"
            return Response({"message": f"Account {state}"})

        user.is_active = is_active
        user.save()

        if not is_active:
            userActivation_Task.apply_async(args=[user.id], countdown=10)

        message = "Account activated" if is_active else "Account deactivated (will auto-activate in 10s)"
        return Response({"message": message})

class GetAllUser(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = GetAllUserSerializer
    pagination_class = MyCursorPagination