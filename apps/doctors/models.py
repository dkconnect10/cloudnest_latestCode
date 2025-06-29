from django.db import models
from apps.users.models import User,Role
from apps.Address.models import TimestampAwareModel,Address
from apps.licenses.models import License

  
  
class Doctor(TimestampAwareModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    specialization=models.CharField(max_length=255,null=True,blank=True)
    address=models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    license = models.OneToOneField(License,on_delete=models.CASCADE,null=True,blank=True)
    experience_years=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.user.full_name or self.user.email       