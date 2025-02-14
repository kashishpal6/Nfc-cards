from django.contrib import admin
from .models import CustomUser, OTP, Profile, Company
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'isVerified', 'date_joined', 'last_login')
    search_fields = ['email']
    ordering = ('email',)
    list_filter = ['isVerified']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Permissions'), {'fields': ('is_active', 'isVerified', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp_code', 'created_at', 'expires_at', 'is_expired')
    search_fields = ('user__email', 'otp_code')
    list_filter = ('expires_at',)

    def is_expired(self, obj):
        return obj.is_expired()
    is_expired.boolean = True
    is_expired.short_description = 'Expired'

class ProfileAdmin(admin.ModelAdmin):
    def Profile_pic(self, obj):
     if obj.profile_pic:
        return format_html(f'<img src="{obj.profile_pic.url}" style="max-width:200px; max-height:200px"/>')
     return "No Image"

    list_display = ('user','fullName', 'dob', 'address', 'phone_number','Profile_pic')
    search_fields = ('user__email', 'fullName','phone_number')
    list_filter = ['user__isVerified','fullName']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'industry', 'designation', 'location', 'user')
    search_fields = ('companyName', 'user__email', 'industry')
    list_filter = ('industry', 'location')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OTP, OTPAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Company, CompanyAdmin)





