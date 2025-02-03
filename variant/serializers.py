from rest_framework import serializers
from .models import variant


class variantSerializer(serializers.ModelSerializer):
   product_id = serializers.IntegerField(source = "id",read_only = True)

   class Meta:
      model=variant
      fields='__all__'