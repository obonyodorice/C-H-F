# FundsApp/forms.py

from django import forms
from .models import Fund

class FundForm(forms.ModelForm):
    """
    Form for creating and updating Fund objects.
    """
    class Meta:
        model = Fund
        fields = [
            'name', 'description', 'is_active', 'target_amount'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        help_texts = {
            'name': 'Name of the fund (e.g., General Tithes, Thanksgiving Offering).',
            'description': 'Detailed description of the fund\'s purpose.',
            'is_active': 'Indicates if the fund is currently active and accepting contributions.',
            'target_amount': 'Target amount for this fund/campaign (set to 0 if no specific target).',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply custom CSS classes to all fields for consistent styling
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                current_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = current_classes + ' form-control'
            else:
                current_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = current_classes + ' form-check-input'
