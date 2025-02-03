from rest_framework import serializers
from .models import Contact


class contactSerializer(serializers.ModelSerializer):
   contact_id = serializers.IntegerField(source = "id",read_only = True)
   class Meta:
      model=Contact
      fields=['contact_id','Fullname','email','phoneNumber','message']