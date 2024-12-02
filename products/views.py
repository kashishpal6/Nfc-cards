from .models import Products
from .serializers import productSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny


class createProducts(generics.CreateAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [IsAuthenticated]

class listProducts(generics.ListAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [AllowAny]

class RetrieveProducts(generics.RetrieveAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [AllowAny]

class UpdateProducts(generics.UpdateAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [IsAuthenticated]

class DestroyProducts(generics.DestroyAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [IsAuthenticated]
