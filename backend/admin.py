from django.contrib import admin
from .models import FAQ, Employee, Region, EmailForm, NewsType, News, Statistics, UsefulLink, City, Offer

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
    list_display = ('name', 'code', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'code')
    ordering = ('name', '-created_at')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'is_active', 'created_at')
    list_filter = ('region', 'is_active', 'created_at')
    search_fields = ('name', 'region__name')
    ordering = ('name', '-created_at')

@admin.register(NewsType)
class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_type', 'hashtag', 'created_at', 'updated_at')
    list_filter = ('news_type', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'hashtag')
    ordering = ('-created_at',)

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name', '-created_at')

@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'link')
    ordering = ('-created_at',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'region', 'city', 'phone', 'category', 'created_at')
    list_filter = ('category', 'region', 'city', 'created_at')
    search_fields = ('fullname', 'phone', 'message')
    ordering = ('-created_at',)
