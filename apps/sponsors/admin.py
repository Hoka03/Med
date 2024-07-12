from django.contrib import admin

from .models import Sponsor, SponsorStudent


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'amount', 'company_name', 'type_choice', 'status', 'payment_type',
                    'created_at', 'spent_amount')
    list_display_links = list_display
    readonly_fields = ('spent_amount',)
    search_fields = ('full_name', 'phone_number', 'company_name')
    list_per_page = 10


@admin.register(SponsorStudent)
class SponsorStudentAdmin(admin.ModelAdmin):
    list_display = ('sponsor', 'student', 'amount')
    list_display_links = list_display
    search_fields = list_display
    list_per_page = 10
