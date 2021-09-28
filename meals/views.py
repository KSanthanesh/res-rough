from django.shortcuts import render
from django.views import generic
from .models import Meals
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'list.html')


def get_meal_list(request):
    meal_list = Meals.objects.all()

    context = {
        'meal_list': meal_list,
    }

    return render(request, 'list.html', context)


def get_meal_detail(request, slug):
    meal_detail = Meals.objects.all()

    context = {
        'meal_detail': meal_detail,
    }
    return render(request, 'meals/detail.html', context)

# user Registration

def register(request):
    form=UserCreationForm
    if request.method == 'POST':
        signup=UserCreationForm(request.POST)
        if signup.is_valid():
            signup.save()
            messages.success(request, 'User has been successfully Registered.')

    return render(request, 'registration/register.html', {'form': form})
