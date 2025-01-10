from .serializers import AddToCartSerializer,GetCartSerializer
from .models import Cart
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class createCart(generics.CreateAPIView):
   queryset=Cart.objects.all()
   serializer_class=AddToCartSerializer
   permission_classes= [IsAuthenticated]

   def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class listCart(generics.ListAPIView):
   queryset=Cart.objects.all()
   serializer_class=GetCartSerializer
   permission_classes= [IsAuthenticated]

   def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class RetrieveCart(generics.RetrieveAPIView):
   queryset=Cart.objects.all()
   serializer_class=GetCartSerializer
   permission_classes= [IsAuthenticated]

class UpdateCart(generics.UpdateAPIView):
    queryset=Cart.objects.all()
    serializer_class=AddToCartSerializer
    permission_classes= [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class DestroyCart(generics.DestroyAPIView):
   queryset=Cart.objects.all()
   serializer_class=AddToCartSerializer
   permission_classes= [IsAuthenticated]

   







