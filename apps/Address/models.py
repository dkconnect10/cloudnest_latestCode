from django.db import models

class TimestampAwareModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(TimestampAwareModel):
    address = models.CharField(max_length=255,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    pincode=models.IntegerField()
    
    def __str__(self):
        return self.address


