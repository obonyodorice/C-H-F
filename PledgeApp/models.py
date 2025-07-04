from django.db import models
from django.utils import timezone # Required for default=timezone.now

# IMPORTANT: Importing Member from the 'Members' app and Fund from the 'Funds' app.
from MembersApp.models import Member
from FundsApp.models import Fund


class Pledge(models.Model):
    """
    Represents a commitment (pledge) made by a donor to contribute a certain amount to a specific fund.
    This model supports listing, creating, viewing details, updating, and deleting pledges
    as per the defined URL patterns.
    """
    FREQUENCY_CHOICES = [
        ('one_time', 'One-time'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually'),
        ('other', 'Other'),
    ]

    # Foreign Key to link this pledge to a specific Member (Donor).
    # 'on_delete=models.CASCADE' means if a Member is deleted, all their
    # associated Pledge records will also be deleted.
    # 'related_name' allows easy reverse lookup from a Member object (e.g., member_instance.pledges.all()).
    donor = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='pledges',
        help_text="The member/donor who made this pledge."
    )

    # Foreign Key to link this pledge to a specific Fund.
    # 'on_delete=models.CASCADE' means if a Fund is deleted, all pledges
    # made to that fund will also be deleted.
    # 'related_name' allows easy reverse lookup from a Fund object (e.g., fund_instance.pledges.all()).
    fund = models.ForeignKey(
        Fund,
        on_delete=models.CASCADE,
        related_name='pledges',
        help_text="The fund to which the pledge is directed."
    )

    pledge_amount = models.DecimalField(
        max_digits=15, # Allows for large amounts
        decimal_places=2, # For currency values
        help_text="The total amount pledged."
    )

    pledge_date = models.DateField(
        default=timezone.now, # Sets the date automatically when a pledge is created
        help_text="The date the pledge was made."
    )

    fulfillment_frequency = models.CharField(
        max_length=20,
        choices=FREQUENCY_CHOICES,
        default='one_time',
        help_text="How often the donor intends to fulfill the pledge (e.g., 'Weekly', 'One-time')."
    )

    start_date = models.DateField(
        blank=True,
        null=True,
        help_text="The date when the pledge fulfillment period starts (optional)."
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="The date when the pledge fulfillment period is expected to end (optional)."
    )

    # Fields for auditing creation and last update times.
    created_at = models.DateTimeField(auto_now_add=True) # Automatically sets on creation
    updated_at = models.DateTimeField(auto_now=True)     # Automatically updates on each save

    def __str__(self):
        """
        String representation of the Pledge object, useful for admin and debugging.
        """
        return f"{self.donor.name}'s Pledge to {self.fund.name} for {self.pledge_amount}"

    class Meta:
        """
        Meta options for the Pledge model.
        """
        verbose_name = "Pledge"
        verbose_name_plural = "Pledges"
        # Default ordering for querysets: most recent pledges first.
        ordering = ['-pledge_date']
        # Optional: Add a unique constraint if a donor can only have one active pledge
        # for a specific fund at a given time. This can get complex with date ranges.
        # Example: unique_together = ('donor', 'fund', 'start_date')