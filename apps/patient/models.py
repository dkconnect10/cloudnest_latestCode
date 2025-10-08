from django.db import models
from apps.users.models import User

from django.db import models
from apps.users.models import User
from apps.Address.models import Address
from datetime import date
from apps.Address.models import TimestampAwareModel
bloud_group = [
            ('A+', 'A+'), ('A-', 'A-'),
            ('B+', 'B+'), ('B-', 'B-'),
            ('AB+', 'AB+'), ('AB-', 'AB-'),
            ('O+', 'O+'), ('O-', 'O-')
        ]

marital_state = [('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')]







class Patient(TimestampAwareModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_profiles')
    hospitals = models.ManyToManyField('hospital.Hospital', related_name='patients', blank=True)  
    current_hospital = models.ForeignKey('hospital.Hospital', on_delete=models.SET_NULL,
                                         null=True, blank=True, related_name='current_patients')    
    blood_group = models.CharField(max_length=5,choices=bloud_group,null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=15, null=True, blank=True)
    marital_status = models.CharField(max_length=20,choices=marital_state,null=True, blank=True)
    allergies = models.TextField(null=True, blank=True, help_text="List of any known allergies")
    medical_history = models.TextField(null=True, blank=True, help_text="Past medical history or chronic diseases")
    current_medications = models.TextField(null=True, blank=True, help_text="Details of ongoing medications")
    height_cm = models.FloatField(null=True, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    blood_pressure = models.CharField(max_length=20, null=True, blank=True)
    pulse_rate = models.PositiveIntegerField(null=True, blank=True)
    last_visit_date = models.DateField(null=True, blank=True)
  
    def __str__(self):
        return f"{self.user.full_name or self.user.username})"
