from rest_framework import serializers
from .models import OTP,CustomUser,Profile,Company


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Profile
        fields = ['user','fullName','dob', 'profile_pic', 'address','phone_number']

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
        fields = ['id', 'email',]

class SignupOrLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']

class UserProfileViewSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['profile', 'company']