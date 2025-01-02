from .models import variant
from .serializers import variantSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser


class createVariant(generics.CreateAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [IsAdminUser]

class listVariant(generics.ListAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [AllowAny]

class RetrieveVariant(generics.RetrieveAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [AllowAny]

class ListVariantByProductID(generics.ListAPIView):
   serializer_class = variantSerializer
   permission_classes =[AllowAny]
   
   def get_queryset(self):
      variants_id = self.kwargs['pk']
      return variant.objects.filter(id = variants_id)
   

class UpdateVariant(generics.UpdateAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [IsAdminUser]

class DestroyVariant(generics.DestroyAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [IsAdminUser]