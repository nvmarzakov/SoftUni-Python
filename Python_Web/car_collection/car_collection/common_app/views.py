# common_app>views.py
from django.shortcuts import render

from car_collection.user_profile_app.models import Profile
from car_collection.car_app.models import Car


# Create your views here.
def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'common/index.html', context)


def catalogue(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    context = {
        'profile': profile,
        'cars': cars,
    }
    return render(request, 'common/catalogue.html', context)
