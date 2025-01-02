from .models import Cart
from rest_framework import serializers

class AddToCartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Cart
        fields = ['user','id','variant','front_data','back_data']
    