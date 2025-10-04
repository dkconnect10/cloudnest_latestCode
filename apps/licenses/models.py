from django.db import models
from apps.Address.models import TimestampAwareModel

class License(TimestampAwareModel):
    license_number = models.CharField(max_length=50, unique=True)
    issued_by = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    document = models.FileField(upload_to='licenses/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    remarks = models.TextField(null=True, blank=True)  # optional notes

    def __str__(self):
        return self.license_number

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "License"
        verbose_name_plural = "Licenses"
