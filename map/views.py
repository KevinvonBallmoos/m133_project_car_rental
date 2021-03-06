from django.shortcuts import render, redirect

from cars.views import list_cars
from .models import Map
from cars.models import Cars
from .forms import MapForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def default_map(request):
    """
    shows map
    param: user request
    returns: map.html
    """
    mapbox_access_token = 'pk.eyJ1Ijoic3Vic2NhcGVyIiwiYSI6ImNrZXdpbmpvODQzb2MycnBpb2VjZWVkNGcifQ.UsJOjWVXbrP7wmlIzWb2wQ'
    return render(request, 'functions/map.html', {'mapbox_access_token': mapbox_access_token})


@login_required()
def list_map(request):
    """
    add location
    param: user request
    return: redirect list_cars
    """
    map_form = MapForm()
    if request.method == 'POST':
        map_form = MapForm(request.POST)
    if map_form.is_valid():
        map_form.save()
        messages.success(request, 'Location successfully added')
    return redirect('/functions/list_cars')


@login_required()
def show_map(request, site_id):
    """
    update location
    param: user request, site_id
    returns: show_map.html
    """
    try:
        site = Map.objects.get(pk=site_id)
    except Map.DoesNotExist:
        messages.error(request, 'There is no location with this id!')
        return redirect(list_cars)
    map_form = MapForm(initial={
        'plz': site.plz,
        'location': site.location,
        'address': site.address,
        'country': site.country,
    })
    if request.method == 'POST':
        map_form = MapForm(request.POST, instance=site)
        if map_form.is_valid():
            site.plz = map_form.cleaned_data['plz']
            site.location = map_form.cleaned_data['location']
            site.address = map_form.cleaned_data['address']
            site.country = map_form.cleaned_data['country']
            site.save()
        messages.success(request, 'Location successfully updated.')
    return render(request, 'functions/show_map.html', {'map_form': map_form, 'site': site})


@login_required()
def delete_map(request, site_id):
    """
    delete location
    param: user request, site_id
    return: redirect list_cars
    """
    try:
        site = Map.objects.get(pk=site_id)
        if Cars.objects.filter(location_id=site_id):
            messages.error(request, 'This site is still linked with a car.')
        else:
            site.delete()
            messages.success(request, 'Location successfully deleted.')
    except Map.DoesNotExist:
        messages.error(request, 'There is no location with this id.')
    return redirect('list_cars')
