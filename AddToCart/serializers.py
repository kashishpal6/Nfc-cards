from .models import Cart
from rest_framework import serializers
from variant.models import variant

class AddToCartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Cart
        fields = ['user','id','variant','front_data','back_data']

class GetCartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    variant_name = serializers.SerializerMethodField()
    variant_image = serializers.SerializerMethodField()
    variant_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['user', 'id', 'variant', 'variant_name', 'variant_image', 'variant_price', 'front_data', 'back_data']

    def get_variant_name(self, obj):
        return obj.variant.name if obj.variant else None

    def get_variant_image(self, obj):
        return obj.variant.image.url if obj.variant and obj.variant.image else None

    def get_variant_price(self, obj):
        return obj.variant.price if obj.variant else None
    