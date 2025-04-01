from django.contrib import admin
from .models import FAQ, Employee

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'created_at', 'updated_at')
    list_editable = ('order',)
    search_fields = ('question', 'answer')
    list_filter = ('created_at', 'updated_at')
    ordering = ('order', '-created_at')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position', 'working_day', 'working_hours_start', 'working_hours_end', 'created_at')
    list_filter = ('working_day', 'position', 'created_at')
    search_fields = ('fullname', 'position')
    ordering = ('fullname', '-created_at')
