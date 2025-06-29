from django.db import models
from apps.Address.models import TimestampAwareModel,Address
from apps.users.models import User

class Hospital(TimestampAwareModel):
    name = models.CharField(max_length=200, unique=True)
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    address = models.ForeignKey(Address,on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
