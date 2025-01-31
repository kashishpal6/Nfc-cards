from rest_framework import serializers
from .models import OTP,CustomUser,Profile,Company


class ProfileSerializer(serializers.ModelSerializer):
    
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
        fields = ['fullName','id', 'email',]

class SignupOrLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']

class UserProfileViewSerializer(serializers.Serializer):
    profile = ProfileSerializer()
    company = CompanySerializer()

    def to_representation(self, instance):
        user = instance
        profile_data = Profile.objects.filter(user=user).first()
        company_data = Company.objects.filter(user=user).first()

        return {
            'profile': ProfileSerializer(profile_data).data if profile_data else None,
            'company': CompanySerializer(company_data).data if company_data else None
        }