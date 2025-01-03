from rest_framework import serializers
from .models import OTP,CustomUser,Profile,Company


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['fullName','dob', 'profile_pic', 'address','phone_number']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['companyName', 'industry', 'designation', 'location']

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['otp_code','email']
    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        otp_code = data.get('otp_code')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User not found")

        otp = OTP.objects.filter(user=user).latest('created_at')

        if otp.otp_code != otp_code:
            raise serializers.ValidationError("Invalid OTP")
        
        data['user'] = user
        return data

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['fullName','id', 'email',]

class SignupOrLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']







# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM0Nzc1MjIzLCJpYXQiOjE3MzM0NzkyMjMsImp0aSI6ImE0ODczMzRiMzE4MzQ4ZmM4NjNmMTc0YWNlYjc2ZDI5IiwidXNlcl9pZCI6IjQ2NWNkMmNmLWIyNDYtNDU3NS1iMjA3LTczYzJiZmY5ZWQwMSJ9._-z6L4sg2hp0921qLkXsfv5D9a0Wu0ZdbOvEj-srPRE