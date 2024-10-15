from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from cars.models import Car


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


def profile(request):
    cars = Car.objects.filter(owner=request.user).all()
    return render(request, 'account/account.html', {"cars": cars})
