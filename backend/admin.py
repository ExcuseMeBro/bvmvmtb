from django.contrib import admin
from django.utils.translation import gettext as _
from .models import FAQ, Employee, Region, EmailForm, NewsType, News, Statistics, UsefulLink, City, Offer, OfferStats, Files, FilesCategory, Persons, PersonType, Gallery, Leader, DistrictLeader, About
from .models import Opendata

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

@admin.register(OfferStats)
class OfferStatsAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name', '-created_at')

@admin.register(FilesCategory)
class FilesCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['url'].widget = admin.widgets.AdminFileWidget()
        form.base_fields['url'].help_text = 'Upload a file'
        return form
    
    def save_model(self, request, obj, form, change):
        if 'url' in request.FILES:
            file = request.FILES['url']
            obj.url = f'files/{file.name}'
            # Save the file to the media directory
            import os
            from django.conf import settings
            file_path = os.path.join(settings.MEDIA_ROOT, 'files', file.name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        super().save_model(request, obj, form, change)
    
    def get_fields(self, request, obj=None):
        return ['url', 'title', 'category']

@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ('position', 'type', 'start_hour', 'end_hour', 'phone', 'email', 'created_at')
    list_filter = ('type', 'created_at', 'updated_at')
    search_fields = ('position', 'biography', 'phone', 'email', 'work_experience')
    ordering = ('-created_at',)
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('fullname', 'avatar', 'position', 'type', 'biography')
        }),
        ('Aloqa ma\'lumotlari', {
            'fields': ('phone', 'email', 'telegram', 'start_hour', 'end_hour')
        }),
        ('Faoliyat ma\'lumotlari', {
            'fields': ('work_experience', 'responsibilities')
        }),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(PersonType)
class PersonTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('name',)

@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'region', 'address', 'working_hours_start', 'working_hours_end', 'phone', 'email', 'created_at')
    list_filter = ('region', 'created_at')
    search_fields = ('fullname', 'phone', 'email', 'address')
    ordering = ('fullname', '-created_at')

@admin.register(DistrictLeader)
class DistrictLeaderAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'city', 'phone', 'location_latitude', 'location_longitude', 'created_at')
    list_filter = ('city', 'created_at')
    search_fields = ('fullname', 'phone', 'city__name')
    ordering = ('fullname', '-created_at')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'created_at', 'updated_at')
    list_filter = ('content_type', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('title', 'description', 'content_type')
        }),
        ('Kontent', {
            'fields': ('image', 'video_url'),
            'description': _('Kontent turiga qarab tegishli maydonni to\'ldiring')
        }),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj and obj.content_type == 'photo':
            return (
                fieldsets[0],
                ('Kontent', {'fields': ('image',)}),
            )
        elif obj and obj.content_type == 'video':
            return (
                fieldsets[0],
                ('Kontent', {'fields': ('video_url',)}),
            )
        return fieldsets


@admin.register(Opendata)
class OpendataAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_at')
    search_fields = ('title', 'link')
    ordering = ('-created_at',)
