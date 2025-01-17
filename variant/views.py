from .models import variant
from .serializers import variantSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser
import django_filters

class VariantFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  
    class Meta:
        model = variant
        fields = ['color','shape','orientation','material_type']


class createVariant(generics.CreateAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [IsAdminUser]

class listVariant(generics.ListAPIView):
   queryset=variant.objects.all()
   serializer_class=variantSerializer
   permission_classes= [AllowAny]
   filterset_class = VariantFilter
   
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