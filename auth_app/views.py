from .serializers import SignupSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import OTP
from rest_framework.authtoken.models import Token
from .serializers import SignupSerializer, OTPSerializer

User = get_user_model()

class SignupView(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp = OTP.objects.create(user=user)
            otp.generate_otp()
            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP code is {otp.otp_code}",
                from_email="kashish.palkurmato@gmail.com",
                recipient_list=[user.email],
            )
            return Response({"message": "OTP sent to your email"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 



class VerifyOTPView(GenericAPIView):
    serializer_class = OTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp_code = serializer.validated_data['otp_code']
            try:
                user = User.objects.get(email=email)
                otp = OTP.objects.filter(user=user).latest('created_at')

                if otp.otp_code == otp_code:
                    user.is_active = True
                    user.save()
                    return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)
                return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

