from django.contrib import admin
from.models import Wishlist

class wishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'variant_id')
    search_fields = ['variant_id', 'user']
    list_filter = ['variant_id']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Wishlist, wishlistAdmin)
