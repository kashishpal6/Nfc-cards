from rest_framework import serializers
from .models import Contact


class contactSerializer(serializers.ModelSerializer):
   contact_id = serializers.CharField(source = "id")
   class Meta:
      model=Contact
      fields=['contact_id','Fullname','email','phoneNumber','message']