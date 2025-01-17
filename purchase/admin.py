from django.contrib import admin
from .models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'variant', 'quantity', 'date_time')
    search_fields = ['variant', 'user']
    list_filter = ['variant']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Purchase, PurchaseAdmin)