from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    filter_horizontal = ('users',)
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
