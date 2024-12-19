from django.contrib import admin
from .models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'material_type', 'service', 'description')
    search_fields = ['material_type', 'service__type']
    list_filter = ['service', 'title']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Products, ProductAdmin)
