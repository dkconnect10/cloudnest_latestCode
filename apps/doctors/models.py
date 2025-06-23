from django.db import models
from apps.users.models import User,Role
from apps.Address.models import TimestampAwareModel,Address

    
    
class License(models.Model):
    license_number = models.CharField(max_length=50, unique=True)
    issued_by = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    document = models.FileField(upload_to='licenses/')
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.license_number
       
class Doctor(TimestampAwareModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    specialization=models.CharField(max_length=255,null=True,blank=True)
    address=models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    license = models.OneToOneField('License',on_delete=models.CASCADE)
    experience_years=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.user.full_name or self.user.email       