from .models import variant
from .serializers import variantSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated


class createVariant(generics.CreateAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [IsAuthenticated]

class listVariant(generics.ListAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [AllowAny]

class RetrieveVariant(generics.RetrieveAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [AllowAny]

class UpdateVariant(generics.UpdateAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [IsAuthenticated]

class DestroyVariant(generics.DestroyAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [IsAuthenticated]