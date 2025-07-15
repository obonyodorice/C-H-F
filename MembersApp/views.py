# MembersApp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse # Import reverse for redirects by name
from .models import Member
from .forms import MemberForm # Import the new MemberForm

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
    """Handles the creation of a new member."""
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('members:member_list')) # Redirect to the member list after successful creation
    else:
        form = MemberForm() # Create an empty form for GET request
    context = {'form': form, 'title': 'Add New Member'}
    return render(request, 'members_app/member_form.html', context)

def member_update(request, pk):
    """Handles the updating of an existing member."""
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member) # Populate form with POST data and existing instance
        if form.is_valid():
            form.save()
            return redirect(reverse('members:member_detail', kwargs={'pk': member.pk})) # Redirect to member detail after update
    else:
        form = MemberForm(instance=member) # Populate form with existing member data for GET request
    context = {'form': form, 'title': f'Update Member: {member.name}'}
    return render(request, 'members_app/member_form.html', context)

def member_delete(request, pk):
    """Handles the deletion of a member."""
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect(reverse('members:member_list')) # Redirect to member list after deletion
    context = {
        'member': member,
        'message': f'Are you sure you want to delete member: {member.name}?'
    }
    return render(request, 'members_app/member_confirm_delete.html', context)
