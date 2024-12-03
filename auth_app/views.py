from .serializers import SignupSerializer, OTPSerializer,ProfileSerializer,CompanySerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import OTP,Profile,Company
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny

User = get_user_model()

class SignupView(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        refer = request.GET.get('refer', None)

        if serializer.is_valid():
            user = serializer.save()
            otp = OTP.objects.create(user=user)
            otp.generate_otp() 
            
            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP code is {otp.otp_code}",
                from_email="your_email@gmail.com", 
                recipient_list=[user.email],
            )
            return Response({"message": "OTP sent to your email"}, status=status.HTTP_201_CREATED)
        
        if refer:
            try:
                referrer = User.objects.get(username=refer)
                user.Profile.referrer = referrer.Profile
                user.Profile.save()
            except User.DoesNotExist:
               return Response({"error": "Invalid referrer"}, status=status.HTTP_400_BAD_REQUEST)       

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class VerifyOTPView(GenericAPIView):
    serializer_class = OTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            otp_code = serializer.validated_data['otp_code']

            try:
                otp = OTP.objects.filter(user=user).latest('created_at')
                if otp.is_expired():
                    otp.delete() 
                    new_otp = OTP.objects.create(user=user)
                    new_otp.generate_otp() 

                    send_mail(
                        subject="Your OTP Code",
                        message=f"Your new OTP code is {new_otp.otp_code}",
                        from_email="your_email@gmail.com", 
                        recipient_list=[user.email],
                    )

                    return Response({"message": "OTP expired. A new OTP has been sent to your email."}, status=status.HTTP_400_BAD_REQUEST)

                if otp.otp_code == otp_code:
                    user.is_active = True
                    user.save()
                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)

                    return Response({
                        "message": "OTP verified successfully",
                        "access_token": access_token,
                        "refresh_token": str(refresh)
                    }, status=status.HTTP_200_OK)

                return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

            except OTP.DoesNotExist:
                return Response({"error": "OTP not found for user"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
