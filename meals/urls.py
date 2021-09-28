from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register')
    # path('', views.get_meal_list, name='get_meal_list'),
    # path('', views.get_meal_detail, name='get_meal_detail'),
]
