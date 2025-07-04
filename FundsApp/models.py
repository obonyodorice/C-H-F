from django.db import models
from django.utils import timezone # Import timezone for auto_now_add/auto_now

class Fund(models.Model):
    """
    Represents a specific fund or campaign for which contributions are collected.
    Examples: "General Tithes", "Thanksgiving Offering", "Missions", "Building Fund".
    """
    name = models.CharField(
        max_length=100,
        unique=True, # Fund names should be unique
        help_text="Name of the fund (e.g., 'General Tithes', 'Thanksgiving Offering')."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Detailed description of the fund's purpose."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Indicates if the fund is currently active and accepting contributions."
    )
    target_amount = models.DecimalField(
        max_digits=15, # Allows for large amounts
        decimal_places=2, # For currency values
        default=0.00,
        help_text="Target amount for this fund/campaign (e.g., for a special offering like Thanksgiving). Set to 0 if no specific target."
    )

    # Fields for auditing creation and last update times.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the Fund object, useful for admin and debugging.
        """
        return self.name

    class Meta:
        """
        Meta options for the Fund model.
        """
        verbose_name = "Fund"
        verbose_name_plural = "Funds"
        # Default ordering for querysets: alphabetically by name.
        ordering = ['name']