from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound 

class createPurchase(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if Purchase.objects.filter(user=self.request.user).exists():
            raise NotFound("Purchase failed!")
        return super().perform_create(serializer)
    
class listpurchase(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class =PurchaseSerializer
    permission_classes = [IsAuthenticated]
    
