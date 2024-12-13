from .models import Ticket
from .serializers import ticketSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class createTicket(generics.CreateAPIView):
   queryset=Ticket.objects.all()
   serializer_class=ticketSerializer
   permission_classes= [IsAdminUser]

class listTicket(generics.ListAPIView):
   queryset=Ticket.objects.all()
   serializer_class=ticketSerializer
   permission_classes= [IsAdminUser]

class RetrieveTicket(generics.RetrieveAPIView):
   queryset=Ticket.objects.all()
   serializer_class=ticketSerializer
   permission_classes= [IsAdminUser]

class UpdateTicket(generics.UpdateAPIView):
   queryset=Ticket.objects.all()
   serializer_class=ticketSerializer
   permission_classes= [IsAdminUser]

class DestroyTicket(generics.DestroyAPIView):
   queryset=Ticket.objects.all()
   serializer_class=ticketSerializer
   permission_classes= [IsAdminUser]