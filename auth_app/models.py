from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from auth_app.manager import CustomUserManager
import random
from django.utils.timezone import now
import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None 
    fullName=models.CharField(max_length=250,default="null")
    email = models.EmailField(unique=True, blank=False,default="abc")
    subscribe = models. BooleanField(default=False)
    isVerified=models.BooleanField(default=False)
    
       
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []

class OTP(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=now)

    
    def generate_otp(self):
        self.otp_code = str(random.randint(100000, 999999))
        self.created_at = now()
        self.expires_at = timezone.now() + timedelta(minutes=5)  
        self.save()

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)
    
    def __str__(self):
        return f"OTP for {self.user.email}"
    
class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="profile")
    dob=models.DateField(null=True)
    profile_pic=models.ImageField(blank=True)
    address=models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="Email")


    class Meta:
        ordering = ['user']

    def __str__(self):
        return str(self.user)
    

class Company(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="company")
    companyName=models.CharField(max_length=250)
    industry=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    location=models.CharField(max_length=50)

    class Meta:
        ordering = ['companyName']
    
    def __str__(self):
        return self.companyName
    







