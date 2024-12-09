from django.shortcuts import render
from .models import Services
from .serializers import servicesSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser


class createServices(generics.CreateAPIView):
   queryset=Services.objects.all()
   serializer_class=servicesSerializer
   permission_classes= [IsAdminUser]

class listServices(generics.ListAPIView):
   queryset=Services.objects.all()
   serializer_class=servicesSerializer
   permission_classes= [AllowAny]

class RetrieveServices(generics.RetrieveAPIView):
   queryset=Services.objects.all()
   serializer_class=servicesSerializer
   permission_classes= [AllowAny]

class UpdateServices(generics.UpdateAPIView):
   queryset=Services.objects.all()
   serializer_class=servicesSerializer
   permission_classes= [IsAdminUser]

class DestroyServices(generics.DestroyAPIView):
   queryset=Services.objects.all()
   serializer_class=servicesSerializer
   permission_classes= [IsAdminUser]

