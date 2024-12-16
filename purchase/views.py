from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.exceptions import NotFound


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
    permission_classes = [IsAdminUser]

class Retrievepurchase(generics.RetrieveAPIView):
   queryset=Purchase.objects.all()
   serializer_class=PurchaseSerializer
   permission_classes= [IsAuthenticated]

   def get_object(self):
        try:
            return Purchase.objects.get(user=self.request.user)
        except Purchase.DoesNotExist:
            raise NotFound(detail="Not any Purchase")
    
