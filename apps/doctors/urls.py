from django.urls import path
from .views import Doctors


urlpatterns = [
    path('AddDoctors/',Doctors.as_view(),name='Doctors'),
]
