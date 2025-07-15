# contributions/models.py

from django.db import models
from django.utils import timezone
from MembersApp.models import Member
from FundsApp.models import Fund


class Contribution(models.Model):

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('check', 'Check'),
        ('online', 'Online Transfer/Card'),
        ('mobile_money', 'Mobile Money (e.g., M-Pesa)'),
        ('other', 'Other'),
    ]

    donor = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='contributions',
        help_text="The member/donor who made this contribution."
    )

    fund = models.ForeignKey(
        Fund,
        on_delete=models.CASCADE,
        related_name='contributions',
        help_text="The fund to which this contribution is directed."
    )

    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        help_text="The amount of the contribution."
    )

    contribution_date = models.DateField(
        default=timezone.now,
        help_text="The date the contribution was received."
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default='cash',
        help_text="The method used for this contribution."
    )

    check_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Check number, if payment method is 'Check'."
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Transaction ID for online or mobile money payments."
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Any additional notes about the contribution (e.g., 'anonymous cash donation')."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.donor.name} - {self.fund.name}: {self.amount} on {self.contribution_date}"

    class Meta:

        verbose_name = "Contribution"
        verbose_name_plural = "Contributions"
        ordering = ['-contribution_date', 'donor__name']