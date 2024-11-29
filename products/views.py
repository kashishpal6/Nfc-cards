from .models import Products
from .serializers import productSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated


class createProducts(generics.CreateAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [AllowAny]

class listProducts(generics.ListAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [IsAuthenticated]

class RetrieveUpdateDestroyProducts(generics.RetrieveUpdateDestroyAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [IsAuthenticated]
