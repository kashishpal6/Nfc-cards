from rest_framework import serializers
from .models import Products


class productSerializer(serializers.ModelSerializer):
   product_id = serializers.CharField(source = "id")
   service_id = serializers.CharField(source="service.id")

   class Meta:
      model=Products
      fields=['product_id','title','image','service_id','description','IsPremium']