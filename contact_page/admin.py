from django.contrib import admin
from.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'Fullname', 'email', 'phoneNumber', 'message')
    search_fields = ['Fullname', 'message','email','phoneNumber']
    ordering = ['id']
    
    list_per_page = 20  

admin.site.register(Contact, ContactAdmin)