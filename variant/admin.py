from django.contrib import admin
from.models import variant

class VariantAdmin(admin.ModelAdmin):
    list_display = ('product','color','stock','price','selling_price','front_image','back_image','material_type','shape','orientation')
    search_fields = ['product__title','material_type','orientation','shape']
    list_filter = ['material_type']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(variant,VariantAdmin)
