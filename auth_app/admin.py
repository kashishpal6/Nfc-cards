from django.contrib import admin
from .models import CustomUser, OTP, Profile, Company
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'fullName','isVerified', 'date_joined', 'last_login')
    search_fields = ('email', 'fullName')
    ordering = ('email',)
    list_filter = ('isVerified', 'fullName')

    fieldsets = (
        (None, {'fields': ('email', 'fullName', 'password')}),
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
    list_display = ('user', 'dob', 'address', 'phone_number')
    search_fields = ('user__email', 'phone_number')
    list_filter = ['user__isVerified']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'industry', 'designation', 'location', 'user')
    search_fields = ('companyName', 'user__email', 'industry')
    list_filter = ('industry', 'location')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OTP, OTPAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Company, CompanyAdmin)






