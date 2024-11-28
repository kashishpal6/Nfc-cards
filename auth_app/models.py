from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser,BaseUserManager
import random
from django.utils.timezone import now


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The phone number is required")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)  
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password=password, **extra_fields)
    
        

class CustomUser(AbstractUser):
    username = None  
    phone_number = models.CharField(max_length=15, unique=True,default=0000)
    email = models.EmailField(unique=True, blank=True, null=True)
    subscribe = models. BooleanField(default=False)
       
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'  
    REQUIRED_FIELDS = [] 




class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)


    def generate_otp(self):
        self.otp_code = str(random.randint(100000, 999999))
        self.created_at = now()
        self.save()

