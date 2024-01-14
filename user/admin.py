from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserADmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserADmin):
    '''User admin panel.'''
    model = User
    ordering = ['id']
    list_display = ['phone_number', 'is_staff']
    fieldsets = [
        (None, {'fields': ('phone_number', 'password')}),
        ('Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Dates', {'fields': ('last_login', 'date_joined', 'date_updated')})
    ]
    add_fieldsets = [
        (None, {
            'fields':
            ('phone_number', 'password1', 'password2'),
            'classes': ('wide',),
            }),
        ('Permissions',
            {'fields': ('is_active', 'is_staff', 'is_superuser'),
             'classes': ('wide',)
             }),
    ]

    readonly_fields = [
        'last_login',
        'date_joined',
        'date_updated',
        ]
