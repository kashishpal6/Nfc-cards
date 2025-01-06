from .serializers import AddToCartSerializer
from .models import Cart
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

class createCart(generics.CreateAPIView):
   queryset=Cart.objects.all()
   serializer_class=AddToCartSerializer
   permission_classes= [IsAuthenticated]

   def perform_create(self, serializer):
        # if Cart.objects.filter(user=self.request.user).exists():
        #  raise NotFound("Product already add to cart")
        serializer.save(user=self.request.user)

class listCart(generics.ListAPIView):
   queryset=Cart.objects.all()
   serializer_class=AddToCartSerializer
   permission_classes= [IsAuthenticated]

class RetrieveCart(generics.RetrieveAPIView):
   queryset=Cart.objects.all()
   serializer_class=AddToCartSerializer
   permission_classes= [IsAuthenticated]

   def get_object(self):
        try:
            return Cart.objects.get(user=self.request.user)
        except Cart.DoesNotExist:
            raise NotFound("Product not found in cart")

class UpdateCart(generics.UpdateAPIView):
    queryset=Cart.objects.all()
    serializer_class=AddToCartSerializer
    permission_classes= [IsAuthenticated]

    def get_object(self):
        try:
            return Cart.objects.get(user=self.request.user)
        except Cart.DoesNotExist:
            raise NotFound("Product is saved")

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class DestroyCart(generics.DestroyAPIView):
   queryset=Cart.objects.all()
   serializer_class=AddToCartSerializer
   permission_classes= [IsAuthenticated]

   def get_object(self):
        try:
            return Cart.objects.get(user=self.request.user)
        except Cart.DoesNotExist:
            raise NotFound("Product not found")