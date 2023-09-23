from django.contrib import admin
from .models import donation_payment, donation_detail

class DonationDetailAdminInline(admin.TabularInline):
    model = donation_detail
    readonly_fields = ('donation_payment', 'charity_name',)  # You can add more readonly fields if needed

@admin.register(donation_payment)
class DonationPaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('donation_number', 'date', 'full_name', 'email', 'phone_number', 'donation_total',)
    list_display = ('donation_number', 'date', 'full_name', 'donation_total',)
    list_filter = ('date',)
    search_fields = ('donation_number', 'full_name', 'email')
    date_hierarchy = 'date'
    inlines = [DonationDetailAdminInline]  # Include the inline for donation_detail

# You can add more customizations to the DonationPaymentAdmin class if needed

admin.site.register(donation_detail)  # Register the donation_detail model as well
