from rest_framework import serializers
from .models import ReturnPage

class ReturnPageSerializer(serializers.ModelSerializer):
    class Meta:
       model = ReturnPage
       fields = ['reason','image','return_type','refund_amount']