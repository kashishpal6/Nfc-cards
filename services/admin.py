from django.contrib import admin
from products.models import Products
from .models import Services  
from django.utils.html import format_html

class ProductInline(admin.TabularInline):
    model = Products
    extra = 1  
    list_display = ('id', 'title', 'material_type', 'service', 'description')
    search_fields = ['material_type', 'service']
    list_filter = ['service', 'title']
    ordering = ['id']
    list_per_page = 20  

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

    @staticmethod

    def Description(obj):
        return obj.description[:300] + '...' if len(obj.description) > 50 else obj.description

    def Image(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-width:200px; max-height:200px"/>')

    
    list_display = ('id', 'type', 'Description', 'price','Image')
    search_fields = ['type']
    list_filter = ['type']
    ordering = ['id']
    list_per_page = 20  

admin.site.register(Services, ServiceAdmin)