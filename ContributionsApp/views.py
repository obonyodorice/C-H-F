# contributions/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse # Used for redirects by name
from .models import Contribution
from .forms import ContributionForm
from MembersApp.models import Member
from FundsApp.models import Fund


def index(request):

    return redirect(reverse('contributions:list_contributions'))


def create_contribution(request):

    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the list of contributions after successful creation
            return redirect(reverse('contributions:list_contributions'))
    else:
        form = ContributionForm() # Create an empty form for GET request

    context = {
        'form': form,
        'form_title': 'Add New Contribution'
    }
    return render(request, 'contributions_app/contribution_form.html', context)


def update_contribution(request, id):

    contribution = get_object_or_404(Contribution, id=id)

    if request.method == 'POST':
        # Populate the form with submitted data and link it to the existing instance
        form = ContributionForm(request.POST, instance=contribution)
        if form.is_valid():
            form.save()
           
            return redirect(reverse('contributions:list_contributions'))
    else:
        # For a GET request, create a form pre-filled with the existing contribution's data
        form = ContributionForm(instance=contribution)

    context = {
        'form': form,
        'contribution': contribution, # Pass the instance to the template if needed for display
        'form_title': 'Update Contribution'
    }
    return render(request, 'contributions_app/contribution_form.html', context)


def delete_contribution(request, id):

    contribution = get_object_or_404(Contribution, id=id)

    if request.method == 'POST':
        # Perform the deletion
        contribution.delete()
     
        return redirect(reverse('contributions:list_contributions'))

    
    context = {
        'contribution': contribution, # Pass the instance to the template for display
        'message': f'Are you sure you want to delete the contribution from {contribution.donor.name} for {contribution.amount} to {contribution.fund.name}?'
    }
    return render(request, 'contributions_app/contribution_confirm_delete.html', context)


def list_contributions(request):

    contributions = Contribution.objects.all().order_by('-contribution_date', 'donor__name')
    context = {'contributions': contributions}
    return render(request, 'contributions_app/contribution_list.html', context)

def contribution_detail(request, pk):

    contribution = get_object_or_404(Contribution, pk=pk)
    context = {'contribution': contribution}
    return render(request, 'contributions_app/contribution_detail.html', context)