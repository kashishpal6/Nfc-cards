from django.contrib import admin
from .models import variant
from django.utils.html import format_html

class VariantAdmin(admin.ModelAdmin):
    def front_image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px;" />',
            obj.front_image.url
        )

    def back_image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px;" />',
            obj.back_image.url
        )
    
    front_image_tag.short_description = 'Front Image'
    back_image_tag.short_description = 'Back Image'
    
    list_display = ('product', 'color', 'stock', 'price', 'selling_price','front_image_tag', 'back_image_tag')
    
    search_fields = ['product__title']
    list_filter = ['product']
    ordering = ['id']
    list_per_page = 20

admin.site.register(variant, VariantAdmin)

