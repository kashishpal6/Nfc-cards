from django.contrib import admin
from.models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id','user','price','status','payment_method','payment_at','product_variation','UTR')
    search_fields = ['payment_id', 'user','product_variation','payment_method']
    list_filter = ['status','payment_method']
    ordering = ['payment_id']
    
    list_per_page = 20  

admin.site.register(Payment, PaymentAdmin)
