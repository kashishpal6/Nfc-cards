from django.contrib import admin
from .models import Banners
from django.utils.html import format_html

class BannerAdmin(admin.ModelAdmin):
    def Image(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-width:200px; max-height:200px"/>')

    list_display = ('id','type','image')
    search_fields = ['type']
    list_filter = ['type']