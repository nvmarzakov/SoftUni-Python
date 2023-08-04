# user_profile_app>views.py

from django.shortcuts import render, redirect

from car_collection.car_app.models import Car
from car_collection.user_profile_app.forms import ProfileCreateForm, ProfileEditForm
from car_collection.user_profile_app.models import Profile


# Create your views here.
def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue_page')

    context = {
        'form': form,
    }
    return render(request, 'user_profile/profile-create.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    total_price = sum(car.price for car in cars)
    context = {
        'profile': profile,
        'total_price': total_price,
    }
    return render(request, 'user_profile/profile-details.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-edit')

    context = {
        'form': form,
    }
    return render(request, 'user_profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == 'POST':
        Car.objects.all().delete()
        Profile.objects.first().delete()
        return redirect('index_page')
    return render(request, 'user_profile/profile-delete.html')
