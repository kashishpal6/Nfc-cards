from .models import Purchase
from rest_framework import serializers

class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Purchase
        fields = ['user','variant','quantity']
    