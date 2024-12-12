from .models import Payment
from .serializers import paymentSerailizer
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import generics

class createPayment(generics.CreateAPIView):
   queryset=Payment.objects.all()
   serializer_class=paymentSerailizer
   permission_classes= [IsAuthenticated]

class listPayment(generics.ListAPIView):
   queryset =Payment.objects.all()
   serializer_class = paymentSerailizer
   permission_classes = [IsAdminUser]

class updatePayment(generics.UpdateAPIView):
   queryset = Payment.objects.all()
   serializer_class = paymentSerailizer
   permission_classes = [IsAdminUser]

class retrievePayment(generics.RetrieveAPIView):
   queryset = Payment.objects.all()
   serializer_class = paymentSerailizer
   permission_classes = [IsAuthenticated]

class destroyPayment(generics.DestroyAPIView):
   queryset = Payment.objects.all()
   serializer_class = paymentSerailizer
   permission_classes = [IsAuthenticated]
