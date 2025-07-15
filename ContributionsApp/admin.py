# contributions/admin.py

from django.contrib import admin
from .models import Contribution

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('donor', 'fund', 'amount', 'contribution_date', 'payment_method')
    list_filter = ('payment_method', 'contribution_date', 'fund')
    search_fields = ('donor__name', 'fund__name', 'transaction_id', 'notes')
    date_hierarchy = 'contribution_date'
    ordering = ('-contribution_date',)
