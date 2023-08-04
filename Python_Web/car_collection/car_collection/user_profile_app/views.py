# user_profile_app>views.py

from django.shortcuts import render

from car_collection.user_profile_app.models import get_profile_context


# Create your views here.
def profile_create(request):
    return render(request, 'user_profile/profile-create.html')


def profile_details(request):
    return render(request, 'user_profile/profile-details.html', get_profile_context())


def profile_edit(request):
    return render(request, 'user_profile/profile-edit.html')


def profile_delete(request):
    return render(request, 'user_profile/profile-delete.html')
