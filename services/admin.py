from django.contrib import admin
from products.models import Products
from .models import Services  

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
    list_display = ('id', 'type', 'description', 'price', 'image')
    search_fields = ['type']
    list_filter = ['type']
    ordering = ['id']
    list_per_page = 20  

admin.site.register(Services, ServiceAdmin)

