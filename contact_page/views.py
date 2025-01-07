from .models import Contact
from .serializers import contactSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status

class contact_us(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = contactSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        contact_instance = serializer.save()
        subject = f"New Contact Query from {contact_instance.Fullname}"
        message = f"Message from: {contact_instance.email}\n\n{contact_instance.message}"
        from_email = 'webmaster@yourdomain.com'  
        recipient_list = ['kashish.palkurmato@gmail.com'] 

        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class list_contact_us(generics.ListAPIView):
   queryset=Contact.objects.all()
   serializer_class=contactSerializer
   permission_classes= [IsAdminUser]