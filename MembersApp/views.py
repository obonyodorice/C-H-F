from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
# from .forms import MemberForm # You would create this form later

def member_list(request):
    """Displays a list of all members."""
    members = Member.objects.all().order_by('name')
    context = {'members': members}
    return render(request, 'members_app/member_list.html', context)

def member_detail(request, pk):
    """Displays details for a single member."""
    member = get_object_or_404(Member, pk=pk)
    context = {'member': member}
    return render(request, 'members_app/member_detail.html', context)

def member_create(request):
    return render(request, 'members_app/member_form.html', {'message': 'Member creation form (logic to be added)'})


def member_update(request, pk):
    return render(request, 'members_app/member_form.html', {'message': f'Update form for Member ID: {pk} (logic to be added)'})


def member_delete(request, pk):
    return render(request, 'members_app/member_confirm_delete.html', {'message': f'Confirm delete for Member ID: {pk} (logic to be added)'})