from django.shortcuts import render, redirect
from .models import Cars, Map, CarTypes
from .forms import CarForm, CarTypeForm
from map.forms import MapForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

"""Add a new Car"""


def list_cars(request):
    cars = Cars.objects.all()
    sites = Map.objects.all()
    car_form = CarForm()
    map_form = MapForm()
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
    if car_form.is_valid():
        car_form.save()
        messages.success(request, 'Car successfully added')
    return render(request, 'functions/list_cars.html', {'cars': cars, 'car_form': car_form, 'sites': sites, 'map_form':
                                                        map_form})


"""Update car"""


def show_cars(request, car_id):
    try:
        car = Cars.objects.get(pk=car_id)
    except Cars.DoesNotExist:
        messages.error(request, 'There is no car with this id!')
        return redirect(list_cars)
    car_form = CarForm(initial={
        'brand': car.brand,
        'model': car.model,
        'image': car.image,
        'ps': car.ps,
        'details': car.details,
        'location': car.location,
        'types': car.types,
    })
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES, instance=car)
        if car_form.is_valid():
            car.brand = car_form.cleaned_data['brand']
            car.model = car_form.cleaned_data['model']
            car.image = car_form.cleaned_data['image']
            car.ps = car_form.cleaned_data['ps']
            car.details = car_form.cleaned_data['details']
            car.location = car_form.cleaned_data['location']
            car.types = car_form.cleaned_data['types']
            car.save()
        messages.success(request, 'Car successfully updated')
    return render(request, 'functions/show_cars.html', {'car_form': car_form, 'car': car})


"""Update car"""


def delete_cars(request, car_id):
    try:
        car = Cars.objects.get(pk=car_id)
        car.delete()
        messages.success(request, 'Successfully deleted')
    except Cars.DoesNotExist:
        messages.success(request, 'There is no car with this id!')
    return redirect('list_cars')
