from .models import Wishlist
from rest_framework import serializers


class WishlistSerializer(serializers.ModelSerializer):
    wishlist_id = serializers.IntegerField(source='id', read_only=True)     
    user = serializers.PrimaryKeyRelatedField(read_only=True)



    class Meta:
        model = Wishlist
        fields = ['wishlist_id','user','variant_id']