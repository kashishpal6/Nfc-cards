from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import OTP,CustomUser,Profile,Company

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'dob', 'profile_pic', 'address']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['companyName', 'industry', 'designation', 'location']

class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        otp_code = data.get('otp_code')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

        otp = OTP.objects.filter(user=user).latest('created_at')

        if otp.otp_code != otp_code:
            raise serializers.ValidationError("Invalid OTP")
        
        data['user'] = user
        return data

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['name','id', 'email', 'phone_number', 'subscribe']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


