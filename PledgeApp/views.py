from django.shortcuts import render, redirect, get_object_or_404
from .models import Pledge
from .forms import PledgeForm # Import the newly created form
# You might need to import Member and Fund if you want to pass them to context for dropdowns etc.
# from MembersApp.models import Member
# from FundsApp.models import Fund

def pledge_list(request):
    """
    Displays a list of all pledges.
    """
    pledges = Pledge.objects.all().order_by('-pledge_date')
    context = {'pledges': pledges}
    return render(request, 'pledges_app/pledge_list.html', context)

def pledge_detail(request, pk):
    """
    Displays details for a single pledge.
    """
    pledge = get_object_or_404(Pledge, pk=pk)
    context = {'pledge': pledge}
    return render(request, 'pledges_app/pledge_detail.html', context)

def pledge_create(request):
    """
    Handles the creation of a new pledge.
    Displays an empty form on GET, saves new pledge on POST.
    """
    if request.method == 'POST':
        form = PledgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pledges:pledge_list') # Redirect to the pledge list after successful creation
    else:
        form = PledgeForm() # Create an empty form for GET request
    context = {'form': form, 'title': 'Create New Pledge'}
    return render(request, 'pledges_app/pledge_form.html', context)

def pledge_update(request, pk):
    """
    Handles the updating of an existing pledge.
    Displays form with existing data on GET, saves updates on POST.
    """
    pledge = get_object_or_404(Pledge, pk=pk)
    if request.method == 'POST':
        form = PledgeForm(request.POST, instance=pledge) # Populate form with POST data and existing instance
        if form.is_valid():
            form.save()
            return redirect('pledges:pledge_detail', pk=pledge.pk) # Redirect to pledge detail after update
    else:
        form = PledgeForm(instance=pledge) # Populate form with existing pledge data for GET request
    context = {'form': form, 'title': f'Update Pledge for {pledge.donor.name}'}
    return render(request, 'pledges_app/pledge_form.html', context)

def pledge_delete(request, pk):
    """
    Handles the deletion of a pledge.
    Displays confirmation on GET, deletes pledge on POST.
    """
    pledge = get_object_or_404(Pledge, pk=pk)
    if request.method == 'POST':
        pledge.delete()
        return redirect('pledges:pledge_list') # Redirect to pledge list after deletion
    context = {'pledge': pledge}
    return render(request, 'pledges_app/pledge_confirm_delete.html', context)
