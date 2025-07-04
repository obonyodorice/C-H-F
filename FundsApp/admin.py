# Funds/admin.py

from django.contrib import admin
from .models import Fund

@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'is_active', 'target_amount', 'created_at'
    )
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    # You might want to add date_hierarchy if you track fund creation over time
    # date_hierarchy = 'created_at'