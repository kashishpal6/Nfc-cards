from django.contrib import admin
from.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    @staticmethod

    def Message(obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    list_display = ('Fullname','email','phoneNumber','query','Message','status')
    search_fields = ['Fullname','email','phoneNumber']
    list_filter = ['status']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Ticket, TicketAdmin)
