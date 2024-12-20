from django.contrib import admin
from.models import ReturnPage
from django.utils.html import format_html

class ReturnPageAdmin(admin.ModelAdmin):
    @staticmethod

    def Reason(obj):
        return obj.reason[:50] + '...' if len(obj.reason) > 50 else obj.reason
    
    def Image(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-width:200px; max-height:200px"/>')


    list_display = ('purchase_id','user','productCode','Reason','status','return_date','is_eligible','quantity','request_type','Image')
    search_fields = ['reason','user','purchase_id','status']
    list_filter = ['status']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(ReturnPage,ReturnPageAdmin)
