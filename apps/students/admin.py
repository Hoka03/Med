from django.contrib import admin

from .models import University, Student


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('university', 'full_name', 'phone_number', 'level', 'contract', 'sponsored_amount', 'year')
    list_display_links = list_display
    list_filter = ('university', 'level')
    search_fields = ('full_name', 'phone_number')
    list_per_page = 10
