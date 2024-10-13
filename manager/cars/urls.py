from django.urls import path
from . import views

urlpatterns = [
    path('<int:car_id>', views.car_info, name='car_info'),
    path('car_create', views.car_create, name='car_create'),
]