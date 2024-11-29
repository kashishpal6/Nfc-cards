from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import OTP

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


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




    
    

