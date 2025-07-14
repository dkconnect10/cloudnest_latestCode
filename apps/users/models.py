from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from apps.Address.models import TimestampAwareModel,Address




class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not username:
            raise ValueError('Username must be provided')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


def avatar_upload_path(instance, filename):
    return f"avatars/{instance.username}/{filename}"



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to=avatar_upload_path, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male','Male'),('female','Female'),('other','Other')], null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    onboarding_complete = models.BooleanField(default=False)
    signup_source = models.CharField(max_length=20, default='website')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
 


        
class Role(TimestampAwareModel):
    name=models.CharField(max_length=50,null=True,blank=True,unique=True)
    is_active=models.BooleanField(default=False)      
    
    def __str__(self):
        return self.name or "Unnamed Role"

class UserRole(TimestampAwareModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}({self.role.name})"
    
    
    
class UserHospital(TimestampAwareModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    hospital=models.ForeignKey("hospital.Hospital",on_delete=models.CASCADE)        
    
    def __str__(self):
        return f"{self.user.username}({self.hospital})"
    
    
class UserDetails(TimestampAwareModel):
    user_obj=models.OneToOneField('User',on_delete=models.CASCADE,primary_key=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    role=models.ForeignKey(UserRole,on_delete=models.CASCADE)
    hospital = models.ForeignKey(UserHospital, on_delete=models.CASCADE, blank=True, null=True) 
    reporting_to=models.ForeignKey('User',on_delete=models.SET_NULL,blank=True,null=True, 
                                   related_name="subordinates")
    
    
    def __str__(self):
        return f"{self.user_obj.username} ({self.role.name}) ({self.reporting_to.name})"    