from rest_framework import serializers
from .models import Banners

class BannerSerializer(serializers.ModelSerializer):
    banner_id = serializers.CharField(source = "id")
     
    class Meta:
        model = Banners
        fields = ['banner_id','type','image']