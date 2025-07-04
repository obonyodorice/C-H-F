from django.shortcuts import render, redirect, get_object_or_404
from .models import Pledge
def pledge_list(request):
    pledges = Pledge.objects.all().order_by('-pledge_date')
    context = {'pledges': pledges}
    return render(request, 'pledges_app/pledge_list.html', context)

def pledge_detail(request, pk):
    pledge = get_object_or_404(Pledge, pk=pk)
    context = {'pledge': pledge}
    return render(request, 'pledges_app/pledge_detail.html', context)

def pledge_create(request):
    return render(request, 'pledges_app/pledge_form.html', {'message': 'Pledge creation form (logic to be added)'})

def pledge_update(request, pk):
    return render(request, 'pledges_app/pledge_form.html', {'message': f'Update form for Pledge ID: {pk} (logic to be added)'})

def pledge_delete(request, pk):
    return render(request, 'pledges_app/pledge_confirm_delete.html', {'message': f'Confirm delete for Pledge ID: {pk} (logic to be added)'})