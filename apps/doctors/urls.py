from django.urls import path
from apps.doctors.views import *

urlpatterns = [
    # Doctor CRUD
    path('create/',CreateDoctor.as_view(), name='create_doctor'),
    path('list/',GetAllDoctors.as_view(), name='get_all_doctors'),
    path('detail/<int:doctor_id>/',GetDoctorDetail.as_view(), name='get_doctor_detail'),
    path('update/<int:doctor_id>/',UpdateDoctor.as_view(), name='update_doctor'),
    path('delete/<int:doctor_id>/',DeleteDoctor.as_view(), name='delete_doctor'),

    # # Availability
    path('availability/create/',CreateDoctorAvailability.as_view(), name='create_doctor_availability'),
    path('availability/',GetDoctorAvailability.as_view(), name='get_doctor_availability'),
    path('availability/update/<int:availability_id>/',UpdateDoctorAvailability.as_view(), name='update_doctor_availability'),
    path('availability/delete/<int:availability_id>/',DeleteDoctorAvailability.as_view(), name='delete_doctor_availability'),

    # # Appointment
    # path('doctor/<int:doctor_id>/appointment/create/', views.create_appointment, name='create_appointment'),
    # path('doctor/<int:doctor_id>/appointments/', views.get_doctor_appointments, name='get_doctor_appointments'),
    # path('patient/<int:patient_id>/appointments/', views.get_patient_appointments, name='get_patient_appointments'),
    # path('appointment/<int:appointment_id>/status/', views.update_appointment_status, name='update_appointment_status'),
    # path('appointment/<int:appointment_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),

    # # Prescription
    # path('prescription/create/', views.create_prescription, name='create_prescription'),
    # path('prescription/<int:appointment_id>/', views.get_prescription_details, name='get_prescription_details'),
    # path('prescription/<int:prescription_id>/update/', views.update_prescription, name='update_prescription'),

    # # Reviews
    # path('doctor/<int:doctor_id>/review/create/', views.create_doctor_review, name='create_doctor_review'),
    # path('doctor/<int:doctor_id>/reviews/', views.get_doctor_reviews, name='get_doctor_reviews'),
    # path('doctor/<int:doctor_id>/rating/', views.get_average_rating, name='get_average_rating'),
]
