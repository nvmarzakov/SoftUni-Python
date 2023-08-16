from django.shortcuts import render, redirect

from .forms import ProfileCreateForm, ProfileEditForm
from .models import ProfileModel
from ..events_app.models import EventModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


# Create your views here.
def create_profile(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard-page')

    context = {
        'form': form,
    }
    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    events = EventModel.objects.count()
    profile = get_profile()
    context = {
        'events': events,
        'profile': profile,
    }
    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = ProfileModel.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details-page')

    context = {
        'form': form,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = ProfileModel.objects.first()
    events = EventModel.objects.all()

    if request.method == 'POST':
        profile.delete()
        events.delete()
        return redirect('home-page')

    return render(request, 'profiles/profile-delete.html')
