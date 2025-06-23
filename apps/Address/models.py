from django.db import models
from django.utils import timezone

class TimestampAwareModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(TimestampAwareModel):
    address = models.CharField(max_length=255,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    pincode=models.IntegerField()


