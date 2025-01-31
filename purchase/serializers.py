from .models import Purchase
from rest_framework import serializers

class PurchaseSerializer(serializers.ModelSerializer):
    Purchase_id = serializers.CharField(source = "id")
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Purchase
        fields = ['user','Purchase_id','variant','quantity','cart_id']
    