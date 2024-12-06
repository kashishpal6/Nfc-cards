from .serializers import OTPSerializer,ProfileSerializer,CompanySerializer,SignupOrLoginSerializer,SignupSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import OTP,Profile,Company,CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny

class SignupOrLoginView(generics.CreateAPIView):
    serializer_class = SignupOrLoginSerializer 
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        user = CustomUser.objects.filter(email=email).first()
        if user:
            OTP.objects.filter(user=user).delete() 
            otp = OTP.objects.create(user=user)
            otp.generate_otp()
            otp.save()
            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP code is {otp.otp_code}",
                from_email="kashish.palkurmato@gmail.com",  
                recipient_list=[user.email],
            )

            return Response({"message": "OTP has been sent to your email."}, status=status.HTTP_200_OK)
        else:
            signup_serializer = SignupOrLoginSerializer(data=request.data)
            if signup_serializer.is_valid():
                user = signup_serializer.save()
                refer = request.data.get('refer')
                if refer:
                    try:
                        referrer = CustomUser.objects.get(username=refer)
                        user.profile.referrer = referrer.profile
                        user.profile.save()
                    except CustomUser.DoesNotExist:
                        return Response({"error": "Invalid referrer"}, status=status.HTTP_400_BAD_REQUEST)
                otp = OTP.objects.create(user=user)
                otp.generate_otp()
                otp.save()

                send_mail(
                    subject="Your OTP Code",
                    message=f"Your OTP code is {otp.otp_code}",
                    from_email="kashish.palkurmato@gmail.com",  
                    recipient_list=[user.email],
                )

                return Response({"message": "OTP has been sent to your email."}, status=status.HTTP_200_OK)
        return Response({"error": "Unexpected error occurred."}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(generics.CreateAPIView):
    serializer_class = OTPSerializer
    queryset = OTP.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            otp_code = serializer.validated_data['otp_code']
            try:
                otp = OTP.objects.filter(user=user).latest('created_at')
                if otp.is_expired():
                    otp.delete() 
                    otp = OTP.objects.create(user=user)  
                    otp.generate_otp() 
                    send_mail(
                        subject="Your OTP Code",
                        message=f"Your new OTP code is {otp.otp_code}",
                        from_email="your_email@example.com",
                        recipient_list=[user.email],
                    )
                    return Response({"message": "OTP expired. A new OTP has been sent to your email."}, status=status.HTTP_200_OK)

                if otp.otp_code == otp_code:
                    user.is_active = True
                    user.save()
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        "message": "OTP verified successfully",
                        "access_token": str(refresh.access_token),
                        "refresh_token": str(refresh)
                    }, status=status.HTTP_200_OK)

                return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

            except OTP.DoesNotExist:
                return Response({"error": "OTP not found for this user"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class listUser(generics.ListAPIView):
   queryset=CustomUser.objects.all()
   serializer_class=SignupSerializer
   permission_classes= [AllowAny]

class createProfile(generics.CreateAPIView):
   queryset=Profile.objects.all()
   serializer_class=ProfileSerializer
   permission_classes= [IsAuthenticated]

class listProfile(generics.ListAPIView):
   queryset=Profile.objects.all()
   serializer_class=ProfileSerializer
   permission_classes= [AllowAny]

class RetrieveProfile(generics.RetrieveAPIView):
   queryset=Profile.objects.all()
   serializer_class=ProfileSerializer
   permission_classes= [AllowAny]

class UpdateProfile(generics.UpdateAPIView):
   queryset=Profile.objects.all()
   serializer_class=ProfileSerializer
   permission_classes= [IsAuthenticated]

class DestroyProfile(generics.DestroyAPIView):
   queryset=Profile.objects.all()
   serializer_class=ProfileSerializer
   permission_classes= [IsAuthenticated]

class createCompany(generics.CreateAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes= [IsAuthenticated]

class listCompany(generics.ListAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes= [AllowAny]

class RetrieveCompany(generics.RetrieveAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes= [AllowAny]

class UpdateCompany(generics.UpdateAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes= [IsAuthenticated]

class DestroyCompany(generics.DestroyAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes= [IsAuthenticated]
