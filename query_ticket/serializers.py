from rest_framework import serializers
from .models import Ticket

class ticketSerializer(serializers.ModelSerializer):
    ticket_id = serializers.IntegerField(source = "id")

    class Meta:
       model = Ticket
       fields = ['ticket_id','query','Fullname','email','message','phoneNumber']