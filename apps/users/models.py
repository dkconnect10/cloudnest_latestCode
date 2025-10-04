from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from apps.Address.models import Address, TimestampAwareModel

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not username:
            raise ValueError("Username must be provided")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, **extra_fields)

def avatar_upload_path(instance, filename):
    return f"avatars/{instance.username}/{filename}"

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to=avatar_upload_path, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[("male","Male"),("female","Female"),("other","Other")], null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    onboarding_complete = models.BooleanField(default=False)
    signup_source = models.CharField(max_length=20, default="website")
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

class Role(TimestampAwareModel):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class UserRole(TimestampAwareModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")

    class Meta:
        unique_together = ("user", "role")

    def __str__(self):
        return f"{self.user.username} ({self.role.name})"
