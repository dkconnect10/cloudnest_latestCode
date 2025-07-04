from django.db import models
from apps.Address.models import TimestampAwareModel,Address
from django.contrib.auth import get_user_model
from apps.licenses.models import License

User = get_user_model()

class Hospital(TimestampAwareModel):
    name = models.CharField(max_length=200, unique=True)
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    address = models.ForeignKey(Address,on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to="hospital_logos/", null=True, blank=True)
    license=models.OneToOneField(License,on_delete=models.CASCADE,null=True,blank=True)
    established_year = models.PositiveIntegerField(null=True, blank=True)
    Approval = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name
