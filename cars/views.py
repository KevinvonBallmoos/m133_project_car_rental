from django.shortcuts import render, redirect
from .models import Cars, Map
from .forms import CarForm
from map .forms import MapForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def list_cars(request):
    cars = Cars.objects.all()
    form = CarForm()
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Car successfully added')
    return render(request, 'functions/list_cars.html', {'cars': cars, 'form': form})


def list_map(request):
    location = Map.objects.all()
    form = MapForm()
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Car successfully added')
    return render(request, 'functions/list_cars.html', {'location': location, 'form': form})


def show_cars(request, cars_id):
    try:
        cars = Cars.objects.get(pk=cars_id)
    except Cars.DoesNotExist:
        messages.error(request, 'There is no car with this id!')
        return redirect(list_cars)
    form = CarForm(initial={
        'brand': cars.brand,
        'model': cars.model,
        'image': cars.image,
        'ps': cars.ps,
        'details': cars.details,
        'location': cars.location,
    })
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=cars)
        if form.is_valid():
            cars.brand = form.cleaned_data['first_name']
            cars.model = form.cleaned_data['last_name']
            cars.image = form.cleaned_data['image']
            cars.ps = form.cleaned_data['ps']
            cars.details = form.cleaned_data['details']
            cars.location = form.cleaned_data['location']
            cars.save()
        messages.success(request, 'Car successfully updated')
    return render(request, 'functions/show_cars.html', {'cars': cars, 'form': form})
