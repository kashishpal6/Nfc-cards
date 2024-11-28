from rest_framework import serializers
from .models import variant


class variantSerializer(serializers.ModelSerializer):

   class Meta:
      model=variant
      fields='__all__'