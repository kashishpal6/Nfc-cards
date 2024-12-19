from django.contrib import admin
from.models import ReturnPage

class ReturnPageAdmin(admin.ModelAdmin):
    list_display = ('purchase_id','user','productCode','image','reason','status','return_date','is_eligible','quantity','request_type')
    search_fields = ['reason','user','purchase_id','status']
    list_filter = ['status']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(ReturnPage,ReturnPageAdmin)
