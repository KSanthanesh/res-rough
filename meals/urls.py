from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('get_meal_list/', views.get_meal_list, name='get_meal_list'),
    path('<slug:slug>/', views.get_meal_detail, name='get_meal_detail'),
 ]
