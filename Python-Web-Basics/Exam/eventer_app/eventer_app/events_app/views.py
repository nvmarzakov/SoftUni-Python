from django.shortcuts import render, redirect

from .forms import EventCreateForm, EventEditForm, EventDeleteForm
from .models import EventModel


# Create your views here.
def dashboard(request):
    events = EventModel.objects.all()

    context = {
        'events': events,
    }
    return render(request, 'events/dashboard.html', context)


def create_event(request):
    form = EventCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard-page')

    context = {
        'form': form,
    }
    return render(request, 'events/event-create.html', context)


def details_event(request, pk):
    event = EventModel.objects.filter(pk=pk).get()

    context = {
        'event': event,
    }

    return render(request, 'events/events-details.html', context)


def edit_event(request, pk):
    event = EventModel.objects.filter(pk=pk).get()
    form = EventEditForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('dashboard-page')

    context = {
        'form': form,
        'event': event,
    }
    return render(request, 'events/event-edit.html', context)


def delete_event(request, pk):
    event = EventModel.objects.filter(pk=pk).get()
    form = EventDeleteForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('dashboard-page')

    context = {
        'form': form,
        'event': event,
    }

    return render(request, 'events/events-delete.html', context)
