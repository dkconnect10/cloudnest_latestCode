from rest_framework.urls import path
from .views import*

urlpatterns = [
    path('create/',CreateHospital.as_view(),name='CreateHospital'),
    path('Hospital_Users/',Hospital_Users.as_view(),name='Hospital_Users'),
    path("update_hospital/",update_Hospital.as_view(),name='update_Hospital'),
    path('HospitalListOrDetailView/',HospitalListOrDetailView.as_view(),name="HospitalListOrDetailView")
]