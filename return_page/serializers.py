from rest_framework import serializers
from .models import ReturnPage

class ReturnPageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
       model = ReturnPage
       fields = ['purchase_id','productCode','reason','image','request_type','quantity','user']