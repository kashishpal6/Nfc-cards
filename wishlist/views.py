from .serializers import WishlistSerializer
from .models import Wishlist
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class createWishlist(generics.CreateAPIView):
   queryset=Wishlist.objects.all()
   serializer_class=WishlistSerializer
   permission_classes= [IsAuthenticated]

   def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class listWishlist(generics.ListAPIView):
   queryset=Wishlist.objects.all()
   serializer_class=WishlistSerializer
   permission_classes= [IsAuthenticated]

   def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

class RetrieveWishlist(generics.RetrieveAPIView):
   queryset=Wishlist.objects.all()
   serializer_class=WishlistSerializer
   permission_classes= [IsAuthenticated]

class UpdateWishlist(generics.UpdateAPIView):
    queryset=Wishlist.objects.all()
    serializer_class=WishlistSerializer
    permission_classes= [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class DestroyWishlist(generics.DestroyAPIView):
   queryset=Wishlist.objects.all()
   serializer_class=WishlistSerializer
   permission_classes= [IsAuthenticated]
