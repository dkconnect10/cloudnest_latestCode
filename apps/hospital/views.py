from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Hospital, UserHospital
from apps.users.models import User, Role, UserRole
from .serializers import *



class CreateHospital(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class HospitalListOrDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, hospital_id=None):
        if hospital_id:
            hospital = get_object_or_404(Hospital, id=hospital_id)
            serializer = HospitalDetailSerializer(hospital)
        else:
            hospitals = Hospital.objects.all()
            serializer = HospitalSerializer(hospitals, many=True)
        return Response({"status": "success", "data": serializer.data})

class UpdateHospital(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        hospital_id = request.data.get("id")
        print("hospital:",hospital_id)
        hospital = get_object_or_404(Hospital, id=hospital_id)
        serializer = HospitalSerializer(hospital, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteHospital(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, hospital_id):
        hospital = get_object_or_404(Hospital, id=hospital_id)
        hospital.delete()
        return Response({"status": "success", "message": "Hospital deleted"}, status=status.HTTP_200_OK)

class ToggleHospitalStatus(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, hospital_id):
        hospital = get_object_or_404(Hospital, id=hospital_id)
        hospital.is_active = not hospital.is_active
        hospital.save()
        return Response({"status": "success", "is_active": hospital.is_active})

class HospitalUserCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = HospitalUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class GetUserAndRole(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, hospital_id):
        print("hospital_id:",hospital_id)
        users = UserHospital.objects.filter(hospital_id=hospital_id).values_list('user', flat=True)
        print("users:",users)
        roles = UserRole.objects.filter(user__in=users)
        serializer = UserRoleSerializer(roles, many=True)
        return Response({"status": "success", "data": serializer.data})

class AssignUserRoleToHospital(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get("user_id")
        role_id = request.data.get("role_id")
        hospital_id = request.data.get("hospital_id")

        if not all([user_id, role_id, hospital_id]):
            return Response({"status": "error", "message": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, id=user_id)
        role = get_object_or_404(Role, id=role_id)
        hospital = get_object_or_404(Hospital, id=hospital_id)

        # Check if user belongs to hospital
        UserHospital.objects.get_or_create(user=user, hospital=hospital)

        # Assign role
        UserRole.objects.get_or_create(user=user, role=role)

        return Response({"status": "success", "message": f"Role '{role.name}' assigned to user '{user.username}'"})

