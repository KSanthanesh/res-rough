from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_list, name='get_list'),
]
