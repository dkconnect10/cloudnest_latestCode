from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,logout,login
from .serializers import UserSerializer,updateUserserializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail  
from django.contrib.auth.tokens import PasswordResetTokenGenerator 
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from src.settings.base import  EMAIL_HOST_USER
from .tasks import userActivation_Task
from .serializers import UserSerializer
from apps.users.swagger_docs.user_swagger import *



class RegisterUser(APIView):
    @register_or_verify_schema()
    def post(self, request):
        uidb64 = request.query_params.get('uidb64')
        verifyed_token = request.query_params.get('verifyed_token')


        if uidb64 and verifyed_token:
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (User.DoesNotExist, ValueError, TypeError):
                return Response({"message": "User not registered"}, status=status.HTTP_401_UNAUTHORIZED)

            token_generator = PasswordResetTokenGenerator()
            if not token_generator.check_token(user, verifyed_token):
                return Response({"message": "Token not valid. Please register again"}, status=status.HTTP_401_UNAUTHORIZED)

            user.is_active = True
            user.is_email_verified = True
            user.save()
            return Response({"message": "User verified successfully"}, status=status.HTTP_202_ACCEPTED)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_instance = serializer.save()
            user_instance.is_active = False
            user_instance.save()

            email = serializer.data.get('email')
            user = User.objects.get(email=email)
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            verify_link = f"http://localhost:3000/verify-email?uid={uid}&token={token}"
            try:
                send_mail(
                    subject='Verify your Email',
                    message=f"Click the link to Verify your Email:\n{verify_link}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
            except Exception as e:
                return Response({"error": f"Failed to send verification email. Reason: {str(e)}"}, status=500)

            return Response({
                "message": "User registered successfully",
                "token": token,
                "uid": uid
            }, status=status.HTTP_201_CREATED)

        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

   
class loginUser(APIView):
    @login_schema()
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request , email=email,password=password)
        if user:
            login(request,user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "status":201,
                "message":"User logged in successfully",
                "user":user.username,
                "access_token":str(refresh.access_token),
                "refresh_Token":str(refresh)
            })
        else:
             return Response({'error': 'Invalid Credentials',"status":401})
                 
class GetProfile(APIView):
    permission_classes = [IsAuthenticated]
    @get_profile_schema
    def get(self,request):
        user = request.user
        print(user)
        serialization = updateUserserializer(user)
        return Response(serialization.data)

class UpdateProfile(APIView):
    permission_classes = [IsAuthenticated]
    @update_profile_schema
    def patch(self, request, pk):
        if not pk:
            return Response({"success": False, "message": "User ID is required.", "status_code": 400}, status=400)

        try:
            user_to_update = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({"success": False, "message": "User not found.", "status_code": 404}, status=404)

        if not request.user.is_superuser and request.user != user_to_update:
            return Response({"success": False, "message": "You are not authorized to update this profile.", "status_code": 403}, status=403)

        serializer = updateUserserializer(user_to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Profile updated successfully.", "status_code": 200}, status=200)

        return Response({"success": False, "message": "Invalid data.", "errors": serializer.errors, "status_code": 400}, status=400)
                    
class logoutUser(APIView):
    permission_classes=[IsAuthenticated]
    @logout_schema
    def post(self,request):
                logout(request)
                return Response({"user profile logout successfully"},status=status.HTTP_200_OK)
            
class ResetPassword(APIView):
    permission_classes=[IsAuthenticated]
    @reset_password_schema
    def post(self,request):
        old_password=request.data.get('old_password')
        new_password=request.data.get('new_password')
        confirm_password=request.data.get('confirm_password')
        user = request.user
        
        if not old_password and not new_password and not confirm_password:
            return Response({"message":"old password , newpassword and confirem password  is rerquired"}, status=status.HTTP_400_BAD_REQUEST)

        if not  new_password == confirm_password:
            return Response({"error": "new password and confirm password do not match."})    
            
        if not check_password(old_password,user.password):
            return Response({"message":"old password is wrong"},status=status.HTTP_404_NOT_FOUND)
        
        user.set_password(new_password)
        user.save()
        
        return Response({"message":"Password update successfully"},status=status.HTTP_200_OK)
       
class forgotPassword(APIView):
    @forgot_password_schema
    def post(self,request):
        email = request.data.get('email')
        uidb64 = request.data.get('uid')
        token = request.data.get('token') 
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password') 
         
        if email and not uidb64 and not token: 
            user = User.objects.filter(email=email).first()
            if not user:
                return Response({"message":"user is not email is not registerd"},status=status.HTTP_404_NOT_FOUND) 
        
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            print(token)
    
            uid = urlsafe_base64_encode(force_bytes(user.pk))  
            reset_link = f"http://yourdomain.com/reset-password?uid={uid}&token={token}"
            try:
                send_mail(
                    subject='Reset Your Password',
                    message=f"Click the link to reset your password:\n{reset_link}",
                    from_email =EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
            except Exception as e:
                  return Response({"error": f"Failed to send verification email. Reason: {str(e)}"}, status=500)
         
            return Response({"message":"Password reset link sent to email.","token":token,"uid":uid}, status=status.HTTP_200_OK)
        elif uidb64 and token and new_password and confirm_password:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.filter(pk=uid).first()   
        
            if not user:
                return Response({"message":"user not register"},status=status.HTTP_401_UNAUTHORIZED)
            token_generator = PasswordResetTokenGenerator()
            authenticated = token_generator.check_token(user,token)

            if not authenticated:
                return Response({"message":"token not valid"},status=status.HTTP_401_UNAUTHORIZED)
            
            if not new_password == confirm_password:
                return Response({"message":"please enter valid confirm_password"},status=status.HTTP_406_NOT_ACCEPTABLE)
            
            user.set_password(new_password)
            user.save()
            
            return Response({"message":"new password set successfully"},status=status.HTTP_200_OK)
        return Response({"error": "Invalid request."}, status=status.HTTP_400_BAD_REQUEST)        

class AccountDeletion(APIView):
    permission_classes=[IsAuthenticated]
    @account_delete_schema
    def post(self,request):
        user = request.user
        
        if user.is_active==False:
            return Response({"message":"User Account alrady Deleted"},status=00)
        
        user.is_active=False
        user.save()
        return Response({"message":"Your Account Delete succesfully"},status=200)
    
class AccountDeactivationReactivation(APIView):
    permission_classes = [IsAuthenticated]
    @account_toggle_schema
    def post(self, request):
        is_active = request.data.get('is_active')
        if is_active is None:
            return Response({"error": "Missing 'is_active' in request body."}, status=400)
        
        user = request.user

        if user.is_active == is_active:
            state = "already active" if is_active else "already deactivated"
            return Response({"message": f"User account is {state}."}, status=200)

        user.is_active = is_active
        user.save()
        
        if not  is_active:
            userActivation_Task.apply_async(args=[user.id],countdown=10)

        message = "User account successfully Activated" if is_active else "User account successfully Deactivated and will auto-activate after 10 second."
        return Response({"message": message}, status=200)

