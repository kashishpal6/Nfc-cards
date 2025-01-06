from .models import Products
from .serializers import productSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser

class createProducts(generics.CreateAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [IsAdminUser]

class listProducts(generics.ListAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [AllowAny]
   

class ListProductsByServiceID(generics.ListAPIView):
    serializer_class = productSerializer
    permission_classes = [AllowAny] 

    def get_queryset(self):
        services_id = self.kwargs['pk'] 
        return Products.objects.filter(service_id=services_id) 


class RetrieveProducts(generics.RetrieveAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [AllowAny]

class UpdateProducts(generics.UpdateAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [IsAdminUser]

class DestroyProducts(generics.DestroyAPIView):
   queryset=Products.objects.all()
   serializer_class=productSerializer
   permission_classes= [IsAdminUser]
