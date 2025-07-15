# MembersApp/forms.py

from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    """
    Form for creating and updating Member objects.
    """
    class Meta:
        model = Member
        fields = [
            'name', 'email', 'phone', 'address',
            'member_id', 'is_active', 'date_joined',
            'family_head', 'notes'
        ]
        widgets = {
            'date_joined': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        help_texts = {
            'name': 'Full name of the member.',
            'email': 'Email address (must be unique if provided).',
            'phone': 'Contact phone number.',
            'address': 'Physical address of the member.',
            'member_id': 'Unique identifier (e.g., envelope number).',
            'is_active': 'Check if the member is currently active.',
            'date_joined': 'Date the member joined.',
            'family_head': 'Select the head of the family if this member is part of a family group.',
            'notes': 'Any additional notes about the member.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply custom CSS classes to all fields for consistent styling
        for field_name, field in self.fields.items():
            # Exclude CheckboxInput from text/select styling, it needs different handling
            if not isinstance(field.widget, forms.CheckboxInput):
                current_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = current_classes + ' form-control' # 'form-control' is a generic class for input styling
            else:
                # For checkboxes, you might want a different class or no class
                current_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = current_classes + ' form-check-input' # Example for checkboxes
