from django.contrib import admin
from .models import FAQ, Employee, Region, EmailForm

@admin.register(EmailForm)
class EmailFormAdmin(admin.ModelAdmin):
    list_display = ('subject', 'first_name', 'last_name', 'email', 'phone', 'region', 'created_at')
    list_filter = ('region', 'created_at')
    search_fields = ('subject', 'first_name', 'last_name', 'email', 'phone')
    ordering = ('-created_at',)

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

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_uz', 'name_ru', 'code', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'name_uz', 'name_ru', 'code')
    ordering = ('name', '-created_at')
