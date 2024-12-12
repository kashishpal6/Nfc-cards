from rest_framework import serializers
from .models import Payment

class paymentSerailizer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
       model = Payment
       fields = '__all__'