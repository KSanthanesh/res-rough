from django.shortcuts import render
from django.views import generic
from .models import Meals


def get_list(request):
    return render(request, 'list.html')


# def get_meal_list(request):
#     meal_list = Meals.objects.all()

#     context = {
#         'meal_list': meal_list,
#     }

#     return render(request, 'list.html', context)


# def get_meal_detail(request,slug):
#     meal_detail = Meals.objects.all()

#     context = {
#         'meal_detail': meal_detail,
#     }
#     return render(request, 'meals/detail.html', context)
