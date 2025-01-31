from .models import Wishlist
from rest_framework import serializers

class WishlistSerializer(serializers.ModelSerializer):
    wishlist_id = serializers.IntegerField(source = "id")
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Wishlist
        fields = ['user','wishlist_id','variant']