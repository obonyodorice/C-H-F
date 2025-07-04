# Pledges/admin.py

from django.contrib import admin
from .models import Pledge

@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = (
        'donor', 'fund', 'pledge_amount', 'pledge_date',
        'fulfillment_frequency', 'start_date', 'end_date', 'created_at'
    )
    list_filter = ('fund', 'fulfillment_frequency', 'pledge_date')
    search_fields = (
        'donor__name', 'fund__name', 'pledge_amount'
    )
    date_hierarchy = 'pledge_date' # Allows easy navigation by date in admin
    # raw_id_fields = ('donor', 'fund') # Useful if you have many members/funds, shows ID input instead of dropdown