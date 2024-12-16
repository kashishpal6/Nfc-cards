from rest_framework import serializers
from .models import ReturnPage

class ReturnPageSerializer(serializers.ModelSerializer):
    class Meta:
       model = ReturnPage
       fields = ['purchase_id','productCode','reason','image','request_type','quantity']