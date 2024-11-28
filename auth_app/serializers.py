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
    class Meta:
        model = OTP
        fields = ['email','otp_code']



    
    

