from django.db import models
from django.utils import timezone # Required for default=timezone.now

class Member(models.Model):
    """
    Represents a church member or donor.
    This model stores personal and contact information for individuals or families who give.
    It supports listing, creating, viewing details, updating, and deleting members
    as per the defined URL patterns.
    """
    name = models.CharField(
        max_length=200,
        help_text="Full name of the church member or donor."
    )
    email = models.EmailField(
        blank=True,
        null=True,
        unique=True, # Ensures each email is unique if provided
        help_text="Email address of the member. Must be unique if provided."
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Phone number of the member."
    )
    address = models.TextField(
        blank=True,
        null=True,
        help_text="Physical address of the member."
    )
    member_id = models.CharField(
        max_length=50,
        unique=True, # Ensures each member has a unique ID if provided
        blank=True,
        null=True,
        help_text="Unique identifier for the member, e.g., envelope number or internal ID."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Indicates if the member is currently active in the church."
    )
    date_joined = models.DateField(
        default=timezone.now, # Sets the date automatically when a member is added
        help_text="Date the member joined or was added to the system."
    )
    # Self-referential ForeignKey to link family members to a primary family head.
    # If a family head is deleted, members linked to them will have their 'family_head' field set to NULL.
    family_head = models.ForeignKey(
        'self', # Refers to the Member model itself
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='family_members', # Allows you to get all members under a family head: family_head_instance.family_members.all()
        help_text="Links to the head of the family, if this member is part of a family group."
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Any additional notes about the member (e.g., spiritual gifts, ministry involvement)."
    )

    # Fields for auditing creation and last update times.
    created_at = models.DateTimeField(auto_now_add=True) # Automatically sets on creation
    updated_at = models.DateTimeField(auto_now=True)     # Automatically updates on each save

    def __str__(self):
        """
        String representation of the Member object.
        This is what will be displayed in the Django admin and when you print a Member object.
        """
        return self.name

    class Meta:
        """
        Meta options for the Member model.
        """
        verbose_name = "Member / Donor"
        verbose_name_plural = "Members / Donors"
        # Default ordering for querysets: alphabetically by name.
        ordering = ['name']