from rest_framework import generics
from .models import Banners
from .serializers import BannerSerializer
from rest_framework.permissions import IsAdminUser

class CreateBanner(generics.CreateAPIView):
    queryset = Banners.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAdminUser]

class UpdateBanner(generics.UpdateAPIView):
   queryset=Banners.objects.all()
   serializer_class=BannerSerializer
   permission_classes= [IsAdminUser]

class DestroyBanner(generics.DestroyAPIView):
   queryset=Banners.objects.all()
   serializer_class=BannerSerializer
   permission_classes= [IsAdminUser]