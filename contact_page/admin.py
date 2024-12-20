from django.contrib import admin
from.models import Contact

class ContactAdmin(admin.ModelAdmin):
    @staticmethod

    def Message(obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    

    list_display = ('id', 'Fullname', 'email', 'phoneNumber', 'Message')
    search_fields = ['Fullname','email','phoneNumber']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Contact, ContactAdmin)

