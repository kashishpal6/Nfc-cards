from django.contrib import admin
from.models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('Fullname','email','phoneNumber','query','message','status')
    search_fields = ['Fullname','email','phoneNumber']
    list_filter = ['status']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Ticket, TicketAdmin)
