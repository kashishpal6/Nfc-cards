from .models import Cart
from rest_framework import serializers
from variant.models import variant

class AddToCartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Cart
        fields = ['user','id','variant','front_data','back_data']

from rest_framework import serializers
from .models import Cart
from variant.models import variant  # Make sure you're importing the correct `variant` model

class GetCartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    variant_name = serializers.SerializerMethodField()
    variant_color = serializers.SerializerMethodField()
    variant_price = serializers.SerializerMethodField()
    variant_front_image = serializers.SerializerMethodField()
    variant_back_image = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['user', 'id', 'variant', 'variant_name', 'variant_color', 'variant_price', 'variant_front_image','variant_back_image','front_data', 'back_data']

    def get_variant_name(self, obj):
        # Retrieve the name of the related variant (assuming `variant.name` exists)
        return obj.variant.product.name if obj.variant else None

    def get_variant_color(self, obj):
        # Retrieve the color from the related variant
        return obj.variant.color if obj.variant else None

    def get_variant_price(self, obj):
        # Retrieve the price from the related variant
        return obj.variant.price if obj.variant else None

    def get_variant_front_image(self, obj):
        # Retrieve the front image URL from the related variant
        return obj.variant.front_image.url if obj.variant and obj.variant.front_image else None

    