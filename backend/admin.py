from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'created_at', 'updated_at')
    list_editable = ('order',)
    search_fields = ('question', 'answer')
    list_filter = ('created_at', 'updated_at')
    ordering = ('order', '-created_at')
