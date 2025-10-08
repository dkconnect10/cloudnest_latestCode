from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Doctor, DoctorAvailability
from .serializers import DoctorSerializer, DoctorAvailabilitySerializer

#Doctor
class CreateDoctor(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = DoctorSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("e",e)
            return Response({"error":"somthing went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetAllDoctors(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        hospital_id = request.query_params.get('hospital_id',None)
        
        if hospital_id:
            doctors = Doctor.objects.filter(hospitals__id = hospital_id)
        else:    
            doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

class GetDoctorDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, doctor_id):
        hospital_id = request.query_params.get('hospital_id',None)
        
        if hospital_id:
            doctor = Doctor.objects.filter(hospitals__in = hospital_id,user=doctor_id)
        else:
            doctor = Doctor.objects.get(user=doctor_id)    
        serializer = DoctorSerializer(doctor)
        return Response({"data": serializer.data, "success": True}, status=status.HTTP_200_OK)

class UpdateDoctor(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, doctor_id):
        doctor = get_object_or_404(Doctor, id=doctor_id)
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

class DeleteDoctor(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, doctor_id):
        doctor = get_object_or_404(Doctor, id=doctor_id)
        doctor.delete()
        return Response({"status": "success", "message": "Doctor deleted"}, status=status.HTTP_200_OK)


#Doctor - Availability
class CreateDoctorAvailability(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            doctor_id = request.data.get("doctor")
            if not doctor_id:
                return Response({"error": "Doctor ID is required"}, status=status.HTTP_400_BAD_REQUEST)

            doctor = get_object_or_404(Doctor, id=doctor_id)
            
            serializer = DoctorAvailabilitySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(doctor=doctor)

            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("Error:", e)
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetDoctorAvailability(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        hospital_id = request.query_params.get('hospital_id',None)
        doctor_id = request.query_params.get('doctor_id',None)
        
        if doctor_id and hospital_id:
            availabilities = DoctorAvailability.objects.filter(doctor=doctor_id,hospital = hospital_id)
        else:
            availabilities = DoctorAvailability.objects.all()    
        
        serializer = DoctorAvailabilitySerializer(availabilities, many=True)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_200_OK)

class UpdateDoctorAvailability(APIView):
    permission_classes=[IsAuthenticated]
    def patch(self,request,availability_id):
        availability = DoctorAvailability.objects.get(id=availability_id)
        
        if not availability:
            return Response({"error":"availablity not presant"},status=status.HTTP_404_NOT_FOUND)
        
        serilizer=DoctorAvailabilitySerializer(availability,data=request.data,partial=True)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response({"success":"Availablity update successfully"},status=status.HTTP_201_CREATED)
        
class DeleteDoctorAvailability(APIView):
    permission_classes=[IsAuthenticated]
    
    def delete(self,request,availability_id):
        availability = DoctorAvailability.objects.get(id=availability_id)
        
        if not availability:
            return Response({
                "error":"availablity not available",
                "success":False
            }
            ,status=status.HTTP_404_NOT_FOUND)
            
        availability.delete()
        
        return Response({
            "message":"availability delete successfully",
            "success":True
            },status=status.HTTP_200_OK)    