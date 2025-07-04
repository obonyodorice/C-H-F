# Members/admin.py

from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'phone', 'member_id', 'is_active',
        'date_joined', 'family_head', 'created_at'
    )
    list_filter = ('is_active', 'date_joined', 'family_head')
    search_fields = ('name', 'email', 'phone', 'member_id', 'address')
    date_hierarchy = 'date_joined' # Allows easy navigation by date in admin
    # raw_id_fields = ('family_head',) # Useful if you have many members, shows ID input instead of dropdown