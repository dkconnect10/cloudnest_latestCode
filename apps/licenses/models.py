from django.db import models
from apps.Address.models import TimestampAwareModel

class License(TimestampAwareModel):
    license_number = models.CharField(max_length=50, unique=True)
    issued_by = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    document = models.FileField(upload_to='licenses/',null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.license_number
       
