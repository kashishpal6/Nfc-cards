from .models import Cart
from rest_framework import serializers
from django.conf import settings

class AddToCartSerializer(serializers.ModelSerializer):
    Cart_id = serializers.IntegerField(source = "id",read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Cart
        fields = ['user','Cart_id','variant','front_data','back_data']

class GetCartSerializer(serializers.ModelSerializer):
    Cart_id = serializers.IntegerField(source = "id",read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    color = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    front_image = serializers.SerializerMethodField()
    back_image = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['user', 'Cart_id','variant','color', 'price','front_image','back_image','front_data','back_data']

    def get_color(self, obj):
        return obj.variant.color
    
    def get_price(self, obj):
        return obj.variant.price
    
    def get_front_image(self, obj):
        return f"{"http://127.0.0.1:8000/"}{obj.variant.front_image.url}"
    
    def get_back_image(self, obj):
        return f"{"http://127.0.0.1:8000/"}{obj.variant.back_image.url}"

  