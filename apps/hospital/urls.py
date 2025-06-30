from rest_framework.urls import path
from .views import CreateHospital

urlpatterns = [
    path('create/',CreateHospital.as_view(),name='CreateHospital')
]