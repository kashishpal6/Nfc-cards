from rest_framework import serializers
from .models import variant


class variantSerializer(serializers.ModelSerializer):
   variant_id = serializers.IntegerField(source = "id",read_only = True)
   product_id = serializers.IntegerField(source = "product.id",read_only = True)

   class Meta:
      model=variant
      fields=['variant_id','product_id','color','stock','price','selling_price','front_image','back_image','material_type','shape','orientation']