# car_app>views.py
from django.shortcuts import render, redirect

from car_collection.car_app.models import Car
from car_collection.user_profile_app.models import Profile
from car_collection.car_app.forms import CarCreateForm, CarEditForm, CarDeleteForm


def car_create(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)  # or None

        if form.is_valid():
            form.save()
            return redirect('catalogue_page')
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car,
    }
    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()
    form = CarEditForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue_page')

    context = {
        'car': car,
        'form': form,
    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()
    # form = CarDeleteForm(request.POST or None, instance=car)
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        car.delete()
        return redirect('catalogue_page')

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-delete.html', context)
