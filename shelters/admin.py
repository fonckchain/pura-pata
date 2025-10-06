from django.contrib import admin
from .models import Shelter


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'phone', 'email', 'is_active', 'created_at']
    list_filter = ['is_active', 'state', 'city']
    search_fields = ['name', 'city', 'state', 'description']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Información General', {
            'fields': ('name', 'description', 'user', 'is_active')
        }),
        ('Ubicación', {
            'fields': ('address', 'city', 'state')
        }),
        ('Contacto', {
            'fields': ('phone', 'email', 'website')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
