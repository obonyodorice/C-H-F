from django import forms
from .models import Contribution

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = [
            'donor', 'fund', 'amount', 'contribution_date',
            'payment_method', 'check_number', 'transaction_id', 'notes'
        ]
        widgets = {
            'contribution_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        help_texts = {
            'donor': 'Select the member who made this contribution.',
            'fund': 'Select the fund this contribution is for (e.g., Thanksgiving Offering).',
            'amount': 'Enter the amount of the contribution.',
            'contribution_date': 'Select the date the contribution was received.',
            'payment_method': 'Choose the method of payment.',
            'check_number': 'Enter the check number if applicable.',
            'transaction_id': 'Enter the transaction ID for online/mobile payments.',
            'notes': 'Add any relevant notes about the contribution.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Add Tailwind CSS classes to form fields for basic styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'