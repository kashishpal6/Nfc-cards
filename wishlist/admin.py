from django.contrib import admin
from.models import Wishlist

class wishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'variant')
    search_fields = ['variant', 'user']
    list_filter = ['variant']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Wishlist, wishlistAdmin)
