from django.shortcuts import render
from cars.models import Car


def index(request):
    cars = Car.objects.all()
    return render(request, 'main/index.html', {'cars': cars})
