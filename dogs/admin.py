from django.contrib import admin
from .models import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'size', 'gender', 'age_years', 'status', 'shelter', 'created_at']
    list_filter = ['status', 'size', 'gender', 'vaccinated', 'sterilized', 'shelter']
    search_fields = ['name', 'breed', 'description']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'description', 'breed', 'age_years', 'age_months', 'size', 'gender', 'color')
        }),
        ('Salud', {
            'fields': ('vaccinated', 'sterilized', 'dewormed', 'special_needs')
        }),
        ('Fotos', {
            'fields': ('photo_main', 'photo_1', 'photo_2', 'photo_3')
        }),
        ('Estado y Relaciones', {
            'fields': ('status', 'shelter', 'publisher', 'is_active')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
