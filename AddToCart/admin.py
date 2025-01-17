from django.contrib import admin
from.models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'variant', 'front_data', 'back_data')
    search_fields = ['variant', 'user']
    list_filter = ['variant']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Cart, CartAdmin)
