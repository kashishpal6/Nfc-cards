from rest_framework import serializers
from .models import Services


class servicesSerializer(serializers.ModelSerializer):
   service_id = serializers.CharField(source = "id")

   class Meta:
      model=Services
      fields=['service_id','type','description','price','image']