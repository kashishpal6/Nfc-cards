from .models import Purchase
from rest_framework import serializers

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['variant','quantity']
    