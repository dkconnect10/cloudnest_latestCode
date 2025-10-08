from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from apps.patient.models import  Patient



class CreatePatientView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        pass