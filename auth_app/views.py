from .serializers import OTPSerializer,ProfileSerializer,CompanySerializer,SignupOrLoginSerializer,SignupSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .models import OTP,Profile,Company,CustomUser
from django.template.loader import render_to_string  
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.exceptions import NotFound

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
            html_message = render_to_string('otp_email_template.html',
                                            {'otp_code': otp.otp_code, 'user_name': user.first_name})
            send_mail(
                subject="Your OTP Code",
                message=f"Your OTP code is {otp.otp_code}",
                from_email="kashish.palkurmato@gmail.com",  
                recipient_list=[user.email],
                html_message=html_message)

            return Response({"message": "OTP has been sent to your email."}, status=status.HTTP_200_OK)
        else:
            signup_serializer = SignupOrLoginSerializer(data=request.data)
            if signup_serializer.is_valid():
                user = signup_serializer.save()
                otp = OTP.objects.create(user=user)
                otp.generate_otp()
                otp.save()
                html_message = render_to_string(
                    'otp_email_template.html',
                    {'otp_code': otp.otp_code, 'user_name': user.first_name})
                send_mail(
                    subject="Your OTP Code",
                    message=f"Your OTP code is {otp.otp_code}",
                    from_email="kashish.palkurmato@gmail.com",  
                    recipient_list=[user.email],html_message=html_message)
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
   permission_classes= [IsAdminUser]

class createProfile(generics.CreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes= [IsAuthenticated]

    def perform_create(self, serializer):
        if Profile.objects.filter(user=self.request.user).exists():
         raise NotFound(detail="Profile already exists")
        serializer.save(user=self.request.user)

class listProfile(generics.ListAPIView):
   queryset=Profile.objects.all()
   serializer_class=ProfileSerializer
   permission_classes= [IsAuthenticated]

class RetrieveProfile(generics.RetrieveAPIView):
   queryset=Profile.objects.all()
   serializer_class=ProfileSerializer
   permission_classes= [IsAuthenticated]

   def get_object(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise NotFound(detail="Profile not found")
        
class UpdateProfile(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Try to get the profile; if not found, create a new one
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def perform_update(self, serializer):
        # Update the profile data
        serializer.save(user=self.request.user)

# class UpdateProfile(generics.UpdateAPIView):
#     queryset=Profile.objects.all()
#     serializer_class=ProfileSerializer
#     permission_classes= [IsAuthenticated]

#     def get_object(self):
#         try:
#             return Profile.objects.get(user=self.request.user)
#         except Profile.DoesNotExist:
#             raise NotFound(detail="Profile not found")

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)

class DestroyProfile(generics.DestroyAPIView):
   queryset=Profile.objects.all()
   serializer_class=ProfileSerializer
   permission_classes= [IsAuthenticated]

   def get_object(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise NotFound(detail="Profile not found")

class createCompany(generics.CreateAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes= [IsAuthenticated]

   def perform_create(self, serializer):
        if Company.objects.filter(user=self.request.user).exists():
         raise NotFound(detail="Company already exists")
        serializer.save(user=self.request.user)

class listCompany(generics.ListAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes= [IsAuthenticated]

class RetrieveCompany(generics.RetrieveAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes= [IsAuthenticated]

   def get_object(self):
        try:
            return Company.objects.get(user=self.request.user)
        except Company.DoesNotExist:
            raise NotFound(detail="Company not found")

class UpdateCompany(generics.UpdateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    permission_classes= [IsAuthenticated]

    def get_object(self):
        try:
            return Company.objects.get(user=self.request.user)
        except Company.DoesNotExist:
            raise NotFound(detail="Company not found")

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class DestroyCompany(generics.DestroyAPIView):
   queryset=Company.objects.all()
   serializer_class=CompanySerializer
   permission_classes= [IsAuthenticated]

   def get_object(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            raise NotFound(detail="Profile not found")
