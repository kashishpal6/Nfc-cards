from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from auth_app.models import CustomUser


class createPurchase(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user  
        serializer.save(user=user)
    
class listpurchase(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class =PurchaseSerializer
    permission_classes = [IsAuthenticated]
    
