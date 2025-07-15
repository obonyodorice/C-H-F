# FundsApp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse # Import reverse for redirects by name
from .models import Fund
from .forms import FundForm # Import the new FundForm

def fund_list(request):
    """Displays a list of all funds."""
    funds = Fund.objects.all().order_by('name')
    context = {'funds': funds}
    return render(request, 'funds_app/fund_list.html', context)

def fund_detail(request, pk):
    """Displays details for a single fund."""
    fund = get_object_or_404(Fund, pk=pk)
    context = {'fund': fund}
    return render(request, 'funds_app/fund_detail.html', context)

def fund_create(request):
    """Handles the creation of a new fund."""
    if request.method == 'POST':
        form = FundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('funds:fund_list')) # Redirect to the fund list after successful creation
    else:
        form = FundForm() # Create an empty form for GET request
    context = {'form': form, 'title': 'Add New Fund'}
    return render(request, 'funds_app/fund_form.html', context)

def fund_update(request, pk):
    """Handles the updating of an existing fund."""
    fund = get_object_or_404(Fund, pk=pk)
    if request.method == 'POST':
        form = FundForm(request.POST, instance=fund) # Populate form with POST data and existing instance
        if form.is_valid():
            form.save()
            return redirect(reverse('funds:fund_detail', kwargs={'pk': fund.pk})) # Redirect to fund detail after update
    else:
        form = FundForm(instance=fund) # Populate form with existing fund data for GET request
    context = {'form': form, 'title': f'Update Fund: {fund.name}'}
    return render(request, 'funds_app/fund_form.html', context)

def fund_delete(request, pk):
    """Handles the deletion of a fund."""
    fund = get_object_or_404(Fund, pk=pk)
    if request.method == 'POST':
        fund.delete()
        return redirect(reverse('funds:fund_list')) # Redirect to fund list after deletion
    context = {
        'fund': fund,
        'message': f'Are you sure you want to delete fund: {fund.name}?'
    }
    return render(request, 'funds_app/fund_confirm_delete.html', context)
