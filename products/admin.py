from django.contrib import admin
from .models import Products
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    def Image(self, obj):
        # Ensure the image field exists in the model and the obj is valid
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="max-width:200px; max-height:200px"/>')
        return 'No Image'  # In case there's no image

    def Description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    
    list_display = ('id', 'title', 'Image', 'service', 'Description', 'IsPremium')
    search_fields = ['service__type']
    list_filter = ['service', 'title']
    ordering = ['id']
    list_per_page = 20  

admin.site.register(Products, ProductAdmin)

