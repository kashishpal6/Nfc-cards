from django.contrib import admin
from products.models import Products
from .models import Services  

class ProductInline(admin.TabularInline):
    model = Products
    extra = 1  

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(Services, ServiceAdmin)

