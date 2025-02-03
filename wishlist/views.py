from .serializers import WishlistSerializer
from .models import Wishlist
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

class createWishlist(generics.CreateAPIView):
   queryset=Wishlist.objects.all()
   serializer_class=WishlistSerializer
   permission_classes= [IsAuthenticated]

   def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Product added to wishlist successfully.",
            "Wishlist": response.data},
            status=status.HTTP_201_CREATED
        )
   
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

   def update(self, request, *args, **kwargs):
       response = super().update(request, *args, **kwargs)
       return Response(
           {"message":"Product updated successfully.",
            "wishlist" :response.data},
           status=status.HTTP_200_OK
       )

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from .serializers import WishlistSerializer

class DestroyWishlist(generics.DestroyAPIView):
   queryset = Wishlist.objects.all()
   serializer_class = WishlistSerializer
   permission_classes = [IsAuthenticated]


   def destroy(self, request, *args, **kwargs):
      response = super().destroy(request, *args, **kwargs)

      return Response(
            {"message": "Product removed from wishlist successfully."},
            status=status.HTTP_200_OK
        )
