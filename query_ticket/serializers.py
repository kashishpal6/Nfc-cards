from rest_framework import serializers
from .models import Ticket

class ticketSerializer(serializers.ModelSerializer):
    class Meta:
       model = Ticket
       fields = ['query','Fullname','email','message','phoneNumber']