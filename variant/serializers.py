from rest_framework import serializers
from .models import variant


class variantSerializer(serializers.ModelSerializer):
   service_id = serializers.CharField(source = "id")

   class Meta:
      model=variant
      fields='__all__'