from django.shortcuts import render, redirect, get_object_or_404
from .models import Fund

def fund_list(request):
    funds = Fund.objects.all().order_by('name')
    context = {'funds': funds}
    return render(request, 'funds_app/fund_list.html', context)

def fund_detail(request, pk):
    fund = get_object_or_404(Fund, pk=pk)
    context = {'fund': fund}
    return render(request, 'funds_app/fund_detail.html', context)

def fund_create(request):
    return render(request, 'funds_app/fund_form.html', {'message': 'Fund creation form (logic to be added)'})

def fund_update(request, pk):
    return render(request, 'funds_app/fund_form.html', {'message': f'Update form for Fund ID: {pk} (logic to be added)'})

def fund_delete(request, pk):
    return render(request, 'funds_app/fund_confirm_delete.html', {'message': f'Confirm delete for Fund ID: {pk} (logic to be added)'})