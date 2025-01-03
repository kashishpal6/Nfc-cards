from django.contrib import admin
from .models import Products

class ProductAdmin(admin.ModelAdmin):
    @staticmethod

    def Description(obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    
    list_display = ('id', 'title', 'service', 'Description')
    search_fields = ['service__type']
    list_filter = ['service', 'title']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Products, ProductAdmin)
