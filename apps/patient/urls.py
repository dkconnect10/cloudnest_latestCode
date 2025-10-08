from django.urls import path
from .views import *

urlpatterns = [
    path('create/',CreatePatientView.as_view(), name='create-patient'),
    # path('list/', views.ListPatientsView.as_view(), name='list-patients'),
    # path('<int:id>/', views.PatientDetailView.as_view(), name='patient-detail'),
]
