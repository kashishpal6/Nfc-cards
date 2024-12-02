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
   permission_classes= [IsAuthenticated]

class RetrieveUpdateDestroyVariant(generics.RetrieveUpdateDestroyAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [IsAuthenticated]