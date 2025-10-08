from django.db import models
from apps.users.models import User
from apps.Address.models import Address
from apps.licenses.models import License
from apps.users.models import Role
from apps.hospital.models import Hospital


choice = [
            ("Scheduled", "Scheduled"),
            ("Completed", "Completed"),
            ("Cancelled", "Cancelled"),
        ]


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor_profiles")
    specialization = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField(default=0)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    license = models.OneToOneField(License, on_delete=models.CASCADE, null=True, blank=True)
    hospitals = models.ManyToManyField(Hospital, related_name="doctors")  

    def __str__(self):
        return f"{self.user.username} - {self.specialization}"


class DoctorAvailability(models.Model):
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE, related_name="availabilities")
    hospital = models.ForeignKey("hospital.Hospital", on_delete=models.CASCADE, related_name="doctor_availabilities")
    day_of_week = models.CharField(max_length=20)  
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('doctor','hospital', 'day_of_week', 'start_time', 'end_time')

        
        
class Appointment(models.Model):
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey("patient.Patient", on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20,choices=choice,default="Scheduled",)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Appointment with {self.doctor.user.username} - {self.patient.user.username}"



# class Prescription(models.Model):
#     appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name="prescription")
#     prescribed_by = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE)
#     medicines = models.TextField()  # or use a separate Medicine model if you want
#     diagnosis = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Prescription by {self.prescribed_by.user.username} on {self.appointment.appointment_date}"


# class DoctorReview(models.Model):
#     doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE, related_name="reviews")
#     patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
#     rating = models.PositiveIntegerField(default=5)
#     review = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Review for {self.doctor.user.username} - {self.rating}⭐"
