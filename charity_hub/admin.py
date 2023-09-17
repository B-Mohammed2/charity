from django.contrib import admin
from . models import Charity, UserProfile

# Register your models here.

class CharityAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'description',
        'contact_name',
        'website',
        'contact_email',
        'donation_link',
    )

class UserProfileAdmin(admin.ModelAdmin):
     list_display=(
        'first_name',
        'last_name',
        
    )


admin.site.register(Charity, CharityAdmin)
admin.site.register(UserProfile, UserProfileAdmin)