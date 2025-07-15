from django import forms
from .models import Pledge
# You might need to import Member and Fund if they are used in form fields
# from MembersApp.models import Member
# from FundsApp.models import Fund


class PledgeForm(forms.ModelForm):
    """
    Form for creating and updating Pledge objects.
    """
    class Meta:
        model = Pledge
        fields = [
            'donor', 'fund', 'pledge_amount', 'pledge_date',
            'fulfillment_frequency', 'start_date', 'end_date'
        ]
        widgets = {
            'pledge_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'donor': 'Donor',
            'fund': 'Fund',
            'pledge_amount': 'Pledge Amount',
            'pledge_date': 'Date Pledged',
            'fulfillment_frequency': 'Frequency',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }