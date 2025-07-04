from django.contrib import admin
from .models import Contribution # Import the Contribution model from your app's models.py

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contribution model.
    This class defines how the Contribution model will appear and behave
    in the Django administration interface.
    """
    # list_display: Fields to display as columns in the list view of contributions.
    list_display = (
        'donor',             # Displays the __str__ of the related Member
        'fund',              # Displays the __str__ of the related Fund
        'amount',
        'contribution_date',
        'payment_method',
        'check_number',      # Display if available
        'transaction_id',    # Display if available
        'created_at',        # When the record was first created
    )

    # list_filter: Fields that can be used to filter the list of contributions
    # in the right sidebar of the admin change list page.
    list_filter = (
        'fund',              # Filter by fund
        'payment_method',    # Filter by payment method
        'contribution_date', # Filter by date
        'created_at',        # Filter by creation date
    )

    # search_fields: Fields that will be searched when a user types into the
    # search box at the top of the admin change list page.
    # Use double underscores (__) to traverse relationships (e.g., 'donor__name' searches by the donor's name).
    search_fields = (
        'donor__name',       # Search by donor's name
        'fund__name',        # Search by fund's name
        'check_number',
        'transaction_id',
        'notes',             # Search within the notes field
    )

    # date_hierarchy: Adds a date-based drilldown navigation bar at the top
    # of the change list page, useful for browsing contributions by year, month, or day.
    date_hierarchy = 'contribution_date'

    fieldsets = (
        (None, {
            'fields': ('donor', 'fund', 'amount', 'contribution_date', 'payment_method')
        }),
        ('Payment Details', {
            'fields': ('check_number', 'transaction_id', 'notes'),
            'classes': ('collapse',), # Makes this section collapsible
        }),
        ('Audit Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
            'description': 'Automatically managed timestamps.'
        }),
    )
    # Make created_at and updated_at read-only in the admin form
    readonly_fields = ('created_at', 'updated_at',)